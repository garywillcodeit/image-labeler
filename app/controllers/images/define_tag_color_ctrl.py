import os
import json
from app.utils.dir_path import images_data_db_path

auth_color = [
    "red",
    "orange",
    "yellow",
    "green",
    "cyan",
    "blue",
    "magenta",
]


def define_tag_color_ctrl(data):

    image_id = data.get("imageId")
    color = data.get("color")

    if color not in auth_color:
        raise Exception("The chosen color is inappropriate.")

    data_path = os.path.join(images_data_db_path, image_id)

    with open(data_path, "r") as f:
        img_data = json.load(f)

    if img_data["tagColor"] == color:
        img_data["tagColor"] = ""
    else:
        img_data["tagColor"] = color

    with open(data_path, "w") as f:
        json.dump(img_data, f, indent=1)

    return {"color": img_data["tagColor"]}, 200
