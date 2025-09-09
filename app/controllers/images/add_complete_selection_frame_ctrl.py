import os
import json
from app.utils.dir_path import images_data_db_path, labels_db_path
from app.utils.check_existing_img_path import check_existing_img_path
from app.utils.get_data import (
    get_selected_obj_data,
)
from uuid import uuid4


def add_complete_selection_frame_ctrl(image_id):
    path = os.path.join(images_data_db_path, image_id)
    check_existing_img_path(path)

    with open(labels_db_path, "r") as f:
        labels = json.load(f)

    default_label = next(e for e in labels if e["default"])

    frame_data = {
        "top": 0,
        "left": 0,
        "height": 100,
        "width": 100,
        "frameId": str(uuid4()),
        "labelId": default_label["id"],
        "labelName": default_label["name"],
        "show": True,
        "active": True,
    }

    with open(path, "r") as f:
        image = json.load(f)

    image["selectedObjects"].append(frame_data)

    with open(path, "w") as f:
        json.dump(image, f, indent=1)

    label_data = get_selected_obj_data(default_label["id"])

    frame_data = {**frame_data, **label_data}

    return frame_data
