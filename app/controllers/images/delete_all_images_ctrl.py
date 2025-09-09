import os
import shutil
from app.utils.dir_path import images_data_db_path, images_files_db_path


def delete_all_images_ctrl():

    shutil.rmtree(images_data_db_path)
    shutil.rmtree(images_files_db_path)

    os.mkdir(images_data_db_path)
    os.mkdir(images_files_db_path)

    return {"msg": "Images successfully deleted!"}
