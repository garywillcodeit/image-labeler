import os
import json
from uuid import uuid4
from .dir_path import images_data_db_path


def check_img_name(image):

    images_data = os.listdir(images_data_db_path)
    for img_data in images_data:
        img_data_path = os.path.join(images_data_db_path, img_data)
        with open(img_data_path, "r") as f:
            data = json.load(f)

        if data["name"] == image["name"]:
            [name, format] = image["name"].split(".")
            image["name"] = f"{name}-{str(uuid4())}.{format}"
            break
