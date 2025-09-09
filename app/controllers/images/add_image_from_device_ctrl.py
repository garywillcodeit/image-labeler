from app.utils.dir_path import images_files_db_path, images_data_db_path
import base64
import os
import json
import io
from PIL import Image
from ..app_init import app_init
from app.utils.resize_img import resize_img
from app.utils.get_image_file import get_image_file
from app.utils.is_allowed_file import is_allowed_file
from app import socketio
import math
from app.utils.check_img_name import check_img_name
from uuid import uuid4
from time import time


def add_image_from_device_ctrl(data):

    app_init()

    images = []

    for i, img in enumerate(data):

        img = data[img]

        if not is_allowed_file(img.filename):
            raise Exception("Invalid image format.")

        name = img.filename
        timestamp = int(time() * 1000)
        filename = str(timestamp)
        format = name.split(".")[-1]
        id = str(uuid4()) + "-" + str(timestamp)
        image_data = {
            "id": id,
            "name": name,
            "date": timestamp,
            "filename": id,
            "format": format,
            "tagColor": None,
            "detectedObjects": [],
            "selectedObjects": [],
        }

        # CHECK IF IMAGE NAME ALREADY EXISTS
        check_img_name(image_data)

        # SAVE IMAGE DATA ON DB
        data_path = os.path.join(images_data_db_path, id)
        with open(data_path, "w") as f:
            json.dump(image_data, f, indent=1)

        # IMAGE TREATMENT
        base64_img_path = os.path.join(images_files_db_path, id)

        image = img.read()

        with Image.open(io.BytesIO(image)) as img:
            if img.mode in ["RGBA", "P", "CMYK"]:
                img = img.convert("RGB")
            new_size = resize_img(img.size)
            img = img.resize(new_size, Image.LANCZOS)
            buffer = io.BytesIO()
            img.save(buffer, format="jpeg")

        base64_img = base64.b64encode(buffer.getvalue()).decode("utf-8")

        with open(base64_img_path, "w") as b:
            b.write(base64_img)

        if i == 0:
            image_data["file"] = get_image_file(image_data["filename"])
            images.insert(0, image_data)
            displayed_img = image_data
        else:
            images.append(image_data)

        progress = str(math.ceil(i / len(data) * 100)) + "%"
        socketio.emit("message", {"data": "Loading image... " + progress})

    count = len(os.listdir(images_data_db_path))

    return {"image": displayed_img, "images": images, "count": count}
