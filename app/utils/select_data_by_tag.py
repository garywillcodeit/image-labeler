import os
import math
import json
from ..utils.dir_path import images_data_db_path
from app import socketio


def select_data_by_tag(tags=[], files_name=[]):
    if len(files_name) == 0:
        files_name = os.listdir(images_data_db_path)

    if len(tags) == 0:
        return files_name

    files = []

    for i, file in enumerate(files_name):
        path = os.path.join(images_data_db_path, file)

        with open(path, "r") as f:
            img_data = json.load(f)

        if img_data["tagColor"] in tags:
            files.append(file)

        progress = str(math.ceil(i / len(files_name) * 100)) + "%"
        socketio.emit("message", {"data": "Selecting the data... " + progress})

    return files
