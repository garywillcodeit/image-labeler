import os
import json
from app.utils.dir_path import images_data_db_path
from app.utils.check_existing_img_path import check_existing_img_path
from app.utils.get_data import get_label_name_by_id


def update_selection_frame_ctrl(image_id, frame_id, frame_data):

    path = os.path.join(images_data_db_path, image_id)

    check_existing_img_path(path)

    with open(path, "r") as f:
        image = json.load(f)

    for i, obj in enumerate(image["selectedObjects"]):
        if obj["frameId"] == frame_id:

            top = frame_data["top"]
            left = frame_data["left"]
            height = frame_data["height"]
            width = frame_data["width"]

            if top < 0:
                top = 0

            if left < 0:
                left = 0

            if height > 100 - top:
                height = 100 - top

            if width > 100 - left:
                width = 100 - left

            image["selectedObjects"][i]["top"] = top
            image["selectedObjects"][i]["left"] = left
            image["selectedObjects"][i]["height"] = height
            image["selectedObjects"][i]["width"] = width

            new_frame_data = image["selectedObjects"][i]

            break

    with open(path, "w") as f:
        json.dump(image, f, indent=1)

    label_id = new_frame_data["labelId"]
    category, name = get_label_name_by_id(label_id)

    if category:
        new_frame_data["labelName"] = category
    else:
        new_frame_data["labelName"] = name

    return new_frame_data
