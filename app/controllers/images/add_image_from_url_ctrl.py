from app.utils.get_timestamp import get_timestamp
from app.utils.dir_path import images_files_db_path, images_data_db_path
import base64
import os
import json
import uuid
import io
import requests
from PIL import Image
from app.utils.resize_img import resize_img
from app.utils.get_image_file import get_image_file
from app.utils.is_valid_url import is_valid_url
from app.utils.is_allowed_file import is_allowed_file
from app.utils.check_img_name import check_img_name


def add_image_from_url_ctrl(data):

    image_url = data["url"]

    # CHECK IF IMG URL IS VALID
    if not is_valid_url(image_url):
        raise Exception("This url is incorrect.")

    # DEFINE IMAGE DATA
    image_url = image_url.split("?")[0]
    name = image_url.split("/")[-1]
    format = name.split(".")[-1]
    timestamp = get_timestamp()
    filename = str(timestamp)
    id = str(uuid.uuid4())

    image_data = {
        "id": id,
        "name": name,
        "date": timestamp,
        "filename": filename,
        "format": format,
        "tagColor": "",
        "detectedObjects": [],
        "selectedObjects": [],
    }

    # CHECK IF IMG FORMAT IS VALID
    if not is_allowed_file(name):
        raise Exception("This file format is not authorized.")

    # CHECK IF IMAGE NAME ALREADY EXISTS
    check_img_name(image_data)

    # SAVE IMAGE DATA
    image_path = os.path.join(images_data_db_path, id)
    with open(image_path, "w") as f:
        json.dump(image_data, f, indent=1)

    # REQUEST IMAGE FILE

    error_msg = "Problem when downloading the image."
    try:

        response = requests.get(image_url)

    except requests.exceptions.RequestException as e:
        if os.path.exists(image_path):
            os.remove(image_path)
        raise Exception(error_msg)

    if response.status_code != 200:
        if os.path.exists(image_path):
            os.remove(image_path)
        raise Exception(error_msg)

    # IMAGE TREATMENT
    try:
        image = Image.open(io.BytesIO(response.content))
        image.verify()
    except (IOError, SyntaxError) as e:
        if os.path.exists(image_path):
            os.remove(image_path)
        raise Exception(error_msg)

    image = response.content

    base64_img_path = os.path.join(images_files_db_path, str(timestamp))

    with Image.open(io.BytesIO(image)) as img:
        if img.mode == "RGBA":
            img = img.convert("RGB")
        new_size = resize_img(img.size)
        img = img.resize(new_size, Image.LANCZOS)
        buffer = io.BytesIO()
        img.save(buffer, format="jpeg")

    base64_img = base64.b64encode(buffer.getvalue()).decode("utf-8")

    with open(base64_img_path, "w") as b:
        b.write(base64_img)

    image_data["file"] = get_image_file(image_data["filename"])

    return image_data
