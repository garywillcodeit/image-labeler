import os
import json
from app.utils.dir_path import images_data_db_path
from app.utils.check_existing_img_path import check_existing_img_path


def delete_label_ctrl(image_id, frame_id):
    path = os.path.join(images_data_db_path, image_id)

    check_existing_img_path(path)

    with open(path, "r") as f:
        image = json.load(f)
        for i, frame in enumerate(image["selectedObjects"]):
            if frame["frameId"] == frame_id:
                del image["selectedObjects"][i]
                break

    with open(path, "w") as f:
        json.dump(image, f, indent=1)

    return "", 200
