import os
import json
from app.utils.dir_path import (
    labels_db_path,
)
from app.utils.get_image_file import get_image_file
from app.utils.get_data import get_label_data
from app.controllers.images.get_all_images_ctrl import get_all_images_ctrl


def load_init_data():
    labels = None
    images = []
    image = None

    if os.path.exists(labels_db_path):
        with open(labels_db_path, "r") as f:
            labels = json.load(f)

    images = get_all_images_ctrl()

    if len(images) > 0:
        image = images[0]

        image["file"] = get_image_file(image["filename"])

        image = get_label_data(image)

    return {
        "labels": labels,
        "images": images,
        "activeImg": image,
        "count": len(images),
    }
