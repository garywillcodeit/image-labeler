import os
import json
from app.utils.dir_path import (
    images_data_db_path,
    images_files_db_path,
)


def check_and_delete_image_ctrl(id):

    # DELETE IMAGE
    image = None
    path = os.path.join(images_data_db_path, id)

    if os.path.exists(path):

        with open(path, "r") as f:
            image = json.load(f)

        os.remove(path)
        os.remove(os.path.join(images_files_db_path, image["filename"]))

    return "", 200
