import os


def check_existing_img_path(path):
    if not os.path.exists(path):
        raise Exception("This image does not exist.")
