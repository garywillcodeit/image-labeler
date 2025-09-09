import json
from app.utils.dir_path import labels_db_path


def get_label_ctrl(id):
    label = None
    with open(labels_db_path, "r") as f:
        labels = json.load(f)
        for lab in labels:
            if lab["id"] == int(id):
                label = lab
                break

    if label == None:
        raise Exception("this label does not exist.")
    else:
        return label
