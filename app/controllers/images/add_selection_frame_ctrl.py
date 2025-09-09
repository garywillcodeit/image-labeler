import os
import json
from app.utils.dir_path import images_data_db_path, labels_db_path
from app.utils.check_existing_img_path import check_existing_img_path
from app.utils.get_data import get_label_data


def add_selection_frame_ctrl(image_id, frame_data):
    path = os.path.join(images_data_db_path, image_id)
    check_existing_img_path(path)

    with open(labels_db_path, "r") as f:
        labels = json.load(f)

    for label in labels:
        if label.get("default") and label["default"] == True:
            frame_data["labelId"] = label["id"]
            break

    if frame_data["top"] < 0:
        frame_data["top"] = 0

    if frame_data["left"] < 0:
        frame_data["left"] = 0

    if frame_data["height"] > 100 - frame_data["top"]:
        frame_data["height"] = 100 - frame_data["top"]

    if frame_data["width"] > 100 - frame_data["left"]:
        frame_data["width"] = 100 - frame_data["left"]

    with open(path, "r") as f:
        image = json.load(f)

    image["selectedObjects"].append(frame_data)

    with open(path, "w") as f:
        json.dump(image, f, indent=1)

    image = get_label_data(image)

    return image
