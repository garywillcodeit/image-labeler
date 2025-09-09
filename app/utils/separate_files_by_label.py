import os
import json
import math
from app import socketio
from .dir_path import images_data_db_path


def separate_files_by_label():
    files_name = os.listdir(images_data_db_path)
    separated_files = {}

    for i, file in enumerate(files_name):
        path = os.path.join(images_data_db_path, file)
        with open(path, "r") as f:
            img_data = json.load(f)

        if len(img_data["selectedObjects"]) == 0:
            json_data = json.dumps(
                {
                    "msg": "You must add at least one frame at " + img_data["name"],
                    "image_id": img_data["id"],
                }
            )
            raise Exception(json_data)

        for e in img_data["selectedObjects"]:
            existing_id = False
            for id in separated_files:
                if e["labelId"] == id:
                    separated_files[id].append(file)
                    existing_id = True
                    break

            if not existing_id:
                separated_files[e["labelId"]] = [file]

        progress = str(math.ceil(i / len(files_name) * 100)) + "%"
        socketio.emit("message", {"data": "Separating the data... " + progress})

    return separated_files
