import os
import json
from app.utils.dir_path import images_data_db_path
from app.utils.check_existing_img_path import check_existing_img_path


def duplicate_selection_frame_ctrl(image_id, frame_id, frame_data):
    path = os.path.join(images_data_db_path, image_id)
    check_existing_img_path(path)

    with open(path, "r") as f:
        image = json.load(f)

    index = next(
        (i for i, e in enumerate(image["selectedObjects"]) if e["frameId"] == frame_id),
        None,
    )

    image["selectedObjects"].insert(index + 1, frame_data)

    with open(path, "w") as f:
        json.dump(image, f, indent=2)

    return "", 200
