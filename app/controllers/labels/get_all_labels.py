import json
from app.utils.dir_path import labels_db_path


def get_all_labels():

    with open(labels_db_path, "r") as f:
        labels = json.load(f)

    return labels
