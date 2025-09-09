import os
import json
from app.utils.dir_path import images_files_db_path, images_data_db_path
from app.utils.get_image_file import get_image_file
import base64
import io
from PIL import Image


def rotate_image_ctrl(type, image_id):

    # VALIDATOR
    if type not in ["left", "right"]:
        raise Exception("The orientation value is incorrect.")

    # ACCES TO IMAGE DATA
    img_data_path = os.path.join(images_data_db_path, image_id)

    with open(img_data_path, "r") as f:
        img_data = json.load(f)

    # IMAGE PROCESS
    img_file_path = os.path.join(images_files_db_path, img_data["filename"])
    with open(img_file_path, "r") as f:
        decoded_img = base64.b64decode(f.read())

    img_io = io.BytesIO(decoded_img)

    with Image.open(img_io) as img:

        angle = 90 if type == "left" else -90

        img = img.rotate(angle, expand=True)

        processed_img_io = io.BytesIO()
        img.save(processed_img_io, format="JPEG")
        processed_img_io.seek(0)

        image_bytes = processed_img_io.getvalue()
        image_64 = base64.b64encode(image_bytes).decode("utf-8")

    # FRAMES PROCESS
    for i, frame in enumerate(img_data["selectedObjects"]):
        if type == "left":
            newLeft = frame["top"]
            newTop = 100 - frame["width"] - frame["left"]
            newWidth = frame["height"]
            newHeight = frame["width"]

        else:
            newLeft = 100 - frame["top"] - frame["height"]
            newTop = frame["left"]
            newWidth = frame["height"]
            newHeight = frame["width"]

        img_data["selectedObjects"][i]["left"] = newLeft
        img_data["selectedObjects"][i]["top"] = newTop
        img_data["selectedObjects"][i]["width"] = newWidth
        img_data["selectedObjects"][i]["height"] = newHeight

    # DB UPDATE
    with open(img_file_path, "w") as f:
        f.write(image_64)

    with open(img_data_path, "w") as f:
        json.dump(img_data, f, indent=1)

    img_data["file"] = get_image_file(image_id)

    return img_data
