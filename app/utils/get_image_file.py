import os
from .dir_path import images_files_db_path


def get_image_file(filename):
    path = os.path.join(images_files_db_path, filename)
    if os.path.exists(path):
        with open(os.path.join(images_files_db_path, filename), "r") as f:
            return "data:image/jpeg;base64," + f.read()
    else:
        return None
