from app.utils.get_timestamp import get_timestamp
from app.utils.dir_path import tmp_dir_path, images_files_db_path, images_data_db_path
import base64
import os
import json
import uuid
from PIL import Image
from app.utils.resize_img import resize_img
from app.utils.get_image_file import get_image_file


def video_shutter_ctrl(data):

    timestamp = get_timestamp()
    filename = str(timestamp)
    name = "capture-" + filename + ".png"
    id = str(uuid.uuid4())
    image_data = {
        "id": id,
        "name": name,
        "date": timestamp,
        "filename": filename,
        "format": "png",
        "tagColor": "",
        "detectedObjects": [],
        "selectedObjects": [],
    }
    # SAVE IMAGE DATA ON DB
    data_path = os.path.join(images_data_db_path, id)
    with open(data_path, "w") as f:
        json.dump(image_data, f, indent=1)

    # IMAGE TREATMENT
    image_path = os.path.join(tmp_dir_path, str(timestamp) + ".png")
    converted_img_path = os.path.join(tmp_dir_path, str(timestamp) + ".jpeg")
    base64_img_path = os.path.join(images_files_db_path, str(timestamp))
    image = base64.b64decode(data["image"].split(",")[1])

    with open(image_path, "wb") as f:
        f.write(image)

    with Image.open(image_path) as f:
        if f.mode == "RGBA":
            f = f.convert("RGB")
        new_size = resize_img(f.size)
        f = f.resize(new_size)
        f.save(converted_img_path, format="jpeg")

    with open(converted_img_path, "rb") as f:
        base64_img = base64.b64encode(f.read())
        with open(base64_img_path, "wb") as b:
            b.write(base64_img)

    image = image_data
    image["file"] = get_image_file(image["filename"])

    for path in [image_path, converted_img_path]:
        if os.path.exists(path):
            os.remove(path)

    return image


def is_allowed_file(filename):
    allowed_format = ["png", "jpg", "jpeg", "webp"]
    return True if filename.split(".")[-1].lower() in allowed_format else False
