import os
from app.utils.dir_path import images_data_db_path


def get_images_count_ctrl():
    images = os.listdir(images_data_db_path)
    return {"count": len(images)}
