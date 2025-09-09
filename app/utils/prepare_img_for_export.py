import os
import math
import json
from .create_img_for_json_export import create_img_for_json_export
from .dir_path import images_data_db_path
from app import socketio


def prepare_img_for_export(images):
    index_to_del = []
    imgs_to_export = []

    # PREPARE DATA FOR DOWNLOADING
    for i, img_id in enumerate(images):

        with open(os.path.join(images_data_db_path, img_id), "r") as f:
            img_data = json.load(f)

        image_file = create_img_for_json_export(img_data)

        if image_file != None:
            img_data["image_file"] = image_file
            imgs_to_export.append(img_data)

        else:
            path = os.path.join(images_data_db_path, img_data["id"])
            os.remove(path)
            index_to_del.append(i)

        progress = str(math.ceil(i / len(images) * 100)) + "%"
        socketio.emit("message", {"data": "Preparing the data... " + progress})

    # DELETE INDEX WITHOUT IMAGE FILE
    for i in index_to_del:
        del images[i]

    return imgs_to_export
