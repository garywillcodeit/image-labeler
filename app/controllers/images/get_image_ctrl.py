import os
import json
from app.utils.dir_path import images_data_db_path
from app.utils.get_image_file import get_image_file
from app.utils.get_data import get_label_data


def get_image_ctrl(id):
    path = os.path.join(images_data_db_path, id)

    if not os.path.exists(path):
        raise Exception("This image does not exist.")

    with open(path, "r") as f:
        image = json.load(f)
        image["file"] = get_image_file(image["filename"])

    if image != None:
        image["file"] = get_image_file(image["filename"])
        image = get_label_data(image)

    return image
