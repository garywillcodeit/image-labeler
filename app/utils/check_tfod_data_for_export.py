import os
import json
import math
from app import socketio
from .dir_path import images_data_db_path


def check_tfod_data_for_export(files_name=None):
    if not files_name:
        files_name = os.listdir(images_data_db_path)

    for i, file in enumerate(files_name):
        path = os.path.join(images_data_db_path, file)
        with open(path, "r") as f:
            img_data = json.load(f)

        if len(img_data["selectedObjects"]) == 0:
            json_data = {
                "msg": "You must add at least one frame at " + img_data["name"],
                "imageId": img_data["id"],
            }

            raise Exception(json_data)

        for obj_i, obj in enumerate(img_data["selectedObjects"]):

            if obj["height"] < 0 or obj["width"] < 0:
                json_res = json.dumps(
                    {
                        "msg": f"There is a problem with the object n°{obj_i+1} of {img_data['name']}",
                        "imageId": img_data["id"],
                    }
                )

                raise Exception(json_res)

            if obj["labelId"] == 0 or obj["labelId"] == "0":
                json_res = json.dumps(
                    {
                        "msg": "You must select a label name for " + img_data["name"],
                        "imageId": img_data["id"],
                    }
                )
                raise Exception(json_res)

            if obj["top"] < 0:
                img_data["selectedObjects"][obj_i]["top"] = 0

            if obj["left"] < 0:
                img_data["selectedObjects"][obj_i]["left"] = 0

            if obj["height"] > 100 - obj["top"]:
                img_data["selectedObjects"][obj_i]["height"] = 100 - obj["top"]

            if obj["width"] > 100 - obj["left"]:
                img_data["selectedObjects"][obj_i]["width"] = 100 - obj["left"]

        with open(path, "w") as f:
            json.dump(img_data, f, indent=1)

        progress = str(math.ceil(i / len(files_name) * 100)) + "%"
        socketio.emit("message", {"data": "Checking the data... " + progress})
