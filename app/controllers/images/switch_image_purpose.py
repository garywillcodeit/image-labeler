import os
import json
from app.utils.dir_path import images_data_db_path


def switch_img_purpose_ctrl(id):
    path = os.path.join(images_data_db_path, id)

    if not os.path.exists(path):
        raise Exception("This image does not exist.")

    with open(path, "r") as f:
        image = json.load(f)
        image["purpose"] = "train" if image["purpose"] == "test" else "test"

    with open(path, "w") as f:
        json.dump(image, f, indent=1)

    return image
