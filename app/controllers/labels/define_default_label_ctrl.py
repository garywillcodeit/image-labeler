import json
from app.utils.dir_path import labels_db_path


def define_default_label_ctrl(data):

    id = int(data["id"]) if isinstance(data["id"], str) else data["id"]

    with open(labels_db_path, "r") as f:
        labels = json.load(f)

    for i, label in enumerate(labels):
        labels[i]["default"] = False
        if label["id"] == id:
            labels[i]["default"] = True

    with open(labels_db_path, "w") as f:
        json.dump(labels, f, indent=1)

    return labels
