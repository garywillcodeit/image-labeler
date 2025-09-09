import os
import base64
from io import BytesIO
from PIL import Image, ImageChops
from app import socketio
import math

from ..utils.dir_path import images_files_db_path


def load_base64(path):
    with open(path, "r") as f:
        image1 = base64.b64decode(f.read())
    return Image.open(BytesIO(image1))


def check_existing_img_file(base64_img_path, new_img_data_path):
    all_images = os.listdir(images_files_db_path)

    image1 = load_base64(base64_img_path)

    for i, existing_img in enumerate(all_images):
        if existing_img != base64_img_path.split("/")[-1]:
            existing_path = os.path.join(images_files_db_path, existing_img)
            image2 = load_base64(existing_path)

            diff = ImageChops.difference(image1, image2)

            if diff.getbbox() is None:
                for path in [base64_img_path, new_img_data_path]:
                    if os.path.exists(path):
                        os.remove(path)
                raise Exception("This image has already been added.")
        progress = str(math.ceil(i / len(all_images) * 100)) + "%"
        socketio.emit("message", {"data": "Checking duplicate... " + progress})
