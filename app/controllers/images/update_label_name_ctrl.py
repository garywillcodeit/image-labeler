import os
import json
from app.utils.dir_path import images_data_db_path, labels_db_path
from app.utils.check_existing_img_path import check_existing_img_path
from app.utils.get_data import get_selected_obj_data


def update_label_name_ctrl(image_id, frame_id, data):
    path = os.path.join(images_data_db_path, image_id)
    check_existing_img_path(path)

    # UPDATE OBJECT LABEL
    with open(path, "r") as f:
        image = json.load(f)

    with open(labels_db_path, "r") as f:
        labels = json.load(f)

    for i, frame in enumerate(image["selectedObjects"]):
        if frame["frameId"] == frame_id:
            new_label = next(label for label in labels if label["id"] == data["id"])
            image["selectedObjects"][i]["labelId"] = data["id"]
            image["selectedObjects"][i]["labelName"] = new_label["name"]
            break

    with open(path, "w") as f:
        json.dump(image, f, indent=1)

    # UPDATE DEFAULT LABEL

    for i, e in enumerate(labels):
        if e["id"] == data["id"]:
            labels[i]["default"] = True
        else:
            labels[i]["default"] = False

    with open(labels_db_path, "w") as f:
        json.dump(labels, f, indent=1)

    label_data = get_selected_obj_data(data["id"])
    return label_data
