import os
import json
from app.utils.dir_path import images_data_db_path, images_files_db_path


def get_all_images_ctrl():
    images = []

    images_data = os.listdir(images_data_db_path)
    files = os.listdir(images_files_db_path)

    for i, data in enumerate(images_data):
        path = os.path.join(images_data_db_path, data)

        with open(path, "r") as f:
            json_data = json.load(f)

        if not json_data["filename"] in files:
            os.remove(path)
            continue

        if json_data.get("purpose"):
            del json_data["purpose"]

        if not json_data.get("tagColor"):
            json_data["tagColor"] = ""

        with open(path, "w") as f:
            json.dump(json_data, f, indent=1)

        images.append(json_data)

    if len(images) > 0:
        images = sorted(images, key=lambda x: (x["tagColor"], x["date"]))

    return images
