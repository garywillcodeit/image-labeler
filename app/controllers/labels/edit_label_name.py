import json
from app.utils.dir_path import labels_db_path


def edit_label_name_ctrl(id, data):

    if data["label"] == None or len(data["label"].strip()) == 0:
        raise Exception("You must write a name.")

    with open(labels_db_path, "r") as f:
        labels = json.load(f)

    for label in labels:
        if label["id"] == int(id):
            label["name"] = data["label"].strip()
            break

    with open(labels_db_path, "w") as f:
        json.dump(labels, f, indent=1)

    return {"msg": "Label successfully updated!"}
