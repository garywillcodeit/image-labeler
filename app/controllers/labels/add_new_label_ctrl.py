import json
from app.utils.dir_path import labels_db_path


def add_new_label(data):

    if data["label"] == None or len(data["label"].strip()) == 0:
        raise Exception("You must write a name.")

    with open(labels_db_path, "r") as f:
        labels = json.load(f)

    for lab in labels:

        if data["label"] == lab["name"]:
            raise Exception("This label already exists.")

    label = {
        "id": len(labels) + 1,
        "name": data["label"].strip(),
        "default": len(labels) == 0,
    }

    labels.append(label)

    with open(labels_db_path, "w") as f:
        json.dump(labels, f, indent=1)

    return {"msg": "Label successfully added!", "label": label}
