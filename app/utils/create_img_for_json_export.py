import io
import os
import base64
from PIL import Image
from .dir_path import tmp_dir_path
from .get_image_file import get_image_file


def create_img_for_json_export(img_data):
    image_name = img_data["id"]

    image_base64 = get_image_file(img_data["filename"])

    if image_base64 == None:
        image_file = None
        return image_file

    image_base64 = image_base64.split(",")[1]
    decoded_image = base64.b64decode(image_base64)

    io_byte_img = io.BytesIO(decoded_image)

    tmp_path = os.path.join(tmp_dir_path, image_name + ".jpeg")
    with Image.open(io_byte_img) as img:
        width, height = img.size
        metadata = {"height": height, "width": width}
        match (img.mode):
            case "L":
                metadata["depth"] = "1"
            case "RGB":
                metadata["depth"] = "3"
            case "RGBA" | "CMYK":
                img = img.convert("RGB")
                metadata["depth"] = "3"
            case _:
                raise Exception("Can't find the image's color depth")

        img.save(tmp_path)

    with open(tmp_path, "rb") as f:
        image_base64 = base64.b64encode(f.read()).decode("utf-8")

    os.remove(tmp_path)

    image_file = image_base64

    return image_file
