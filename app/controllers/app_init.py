import os
import json
import shutil
from ..utils.dir_path import (
    images_files_db_path,
    images_data_db_path,
    labels_db_path,
    tmp_dir_path,
    database_path,
)
from ..utils.check_selected_objects import check_selected_objects


def app_init():

    # INIT DIRECTORIES
    for path in [
        database_path,
        images_files_db_path,
        images_data_db_path,
    ]:
        os.makedirs(path, exist_ok=True)

    # INIT  LABELS
    if not os.path.exists(labels_db_path):
        with open(labels_db_path, "w") as f:
            json.dump([], f)

    # INIT TEMPORARY DIR
    if not os.path.exists(tmp_dir_path):
        os.mkdir(tmp_dir_path)
    else:
        shutil.rmtree(tmp_dir_path)
        os.mkdir(tmp_dir_path)

    # INIT SELECTED OBJECTS
    check_selected_objects()
