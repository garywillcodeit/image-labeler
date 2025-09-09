import os
import json
from app.utils.dir_path import images_data_db_path, labels_db_path


def get_training_data_ctrl():
    images = os.listdir(images_data_db_path)
    label_count = 0
    tags = []
    unlabeled = 0
    tag_count = {
        "red": 0,
        "orange": 0,
        "yellow": 0,
        "green": 0,
        "cyan": 0,
        "blue": 0,
        "magenta": 0,
        "untagged": 0,
    }
    images_count = 0

    with open(labels_db_path, "r") as f:
        labels = json.load(f)
        label_count = len(labels)

    for i, label in enumerate(labels):
        labels[i]["count"] = 0

    for img in images:
        images_count += 1
        path = os.path.join(images_data_db_path, img)

        with open(path, "r") as f:
            img_data = json.load(f)

        match (img_data["tagColor"]):
            case "red":
                tag_count["red"] += 1
            case "orange":
                tag_count["orange"] += 1
            case "yellow":
                tag_count["yellow"] += 1
            case "green":
                tag_count["green"] += 1
            case "cyan":
                tag_count["cyan"] += 1
            case "blue":
                tag_count["blue"] += 1
            case "magenta":
                tag_count["magenta"] += 1
            case _:
                tag_count["untagged"] += 1

        if len(img_data["selectedObjects"]) == 0:
            unlabeled += 1

        for obj in img_data["selectedObjects"]:
            for i, label in enumerate(labels):
                if obj["labelId"] == label["id"]:
                    labels[i]["count"] += 1

    tags = [{"tag": e, "count": tag_count[e]} for e in tag_count if tag_count[e] > 0]

    labels = [e for e in labels if e["count"] > 0]

    return {
        "labelCount": label_count,
        "labels": labels,
        "tags": tags,
        "imgCount": images_count,
        "unlabeled": unlabeled,
    }
