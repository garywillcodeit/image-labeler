import os
import json
from .dir_path import images_data_db_path, labels_db_path
from uuid import uuid4


def define_export_file_name():
    # LOAD ALBELS
    with open(labels_db_path, "r") as f:
        labels = json.load(f)

    # LIST IMAGES DATA
    files_list = os.listdir(images_data_db_path)

    # ADD ALL LABEL IDS IN ONE LIST
    label_ids = []

    for file in files_list:
        path = os.path.join(images_data_db_path, file)

        with open(path, "r") as f:
            img_data = json.load(f)

        label_ids += [obj["labelId"] for obj in img_data["selectedObjects"]]

    # DEFINE EXPORT FILE NAME

    if all(id == label_ids[0] for id in label_ids):

        label = next(
            (l for l in labels if l["id"] == label_ids[0]),
            None,
        )
        if label:
            name = label["name"]
            name = name.lower().replace(" ", "-")
            return f"{name}-{str(uuid4())}.json"
    else:
        return f"multiple-labels-{str(uuid4())}.json"
