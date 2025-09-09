import json
from .dir_path import labels_db_path


def get_label_data(image):
    with open(labels_db_path, "r") as f:
        labels = json.load(f)
        for i, frame in enumerate(image["selectedObjects"]):
            for label in labels:
                if label["id"] == frame["labelId"]:
                    image["selectedObjects"][i]["labelName"] = label["name"]
                    break

    return image


def get_selected_obj_data(label_id):

    with open(labels_db_path, "r") as f:
        labels = json.load(f)

    for label in labels:
        if label["id"] == label_id:
            return {"labelName": label["name"], "labelId": label["id"]}


def get_label_name_by_id(id):
    with open(labels_db_path, "r") as f:
        labels = json.load(f)

        for label in labels:
            if label["id"] == id:
                category = label["name"] or None

                return category, label["name"]
                break

    return None
