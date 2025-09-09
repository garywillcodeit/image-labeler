import os
import json
from .dir_path import images_data_db_path
from tqdm import tqdm


def check_selected_objects():
    files_list = os.listdir(images_data_db_path)

    for file in tqdm(
        files_list, total=len(files_list), desc="Init selected objects", unit="image"
    ):
        path = os.path.join(images_data_db_path, file)

        with open(path, "r") as f:
            img_data = json.load(f)

        objects = img_data["selectedObjects"]

        for i, _ in enumerate(objects):
            objects[i]["top"] = objects[i]["top"] if objects[i]["top"] >= 0 else 0
            objects[i]["left"] = objects[i]["left"] if objects[i]["left"] >= 0 else 0
            objects[i]["width"] = (
                objects[i]["width"] if objects[i]["width"] <= 100 else 100
            )
            objects[i]["height"] = (
                objects[i]["height"] if objects[i]["height"] <= 100 else 100
            )

        img_data["selectedObjects"] = objects

        with open(path, "w") as f:
            json.dump(img_data, f, indent=2)
