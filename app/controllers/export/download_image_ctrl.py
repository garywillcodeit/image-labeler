import os
import json
import base64
import io
from app.utils.dir_path import images_data_db_path, images_files_db_path
from flask import send_file


def download_image_ctrl(id):
    data_path = os.path.join(images_data_db_path, id)

    with open(data_path, "r") as f:
        data = json.load(f)

    file_path = os.path.join(images_files_db_path, data["filename"])
    with open(file_path, "r") as f:
        image_b64 = f.read()

    decoded_img = base64.b64decode(image_b64)

    img_io = io.BytesIO()

    img_io.write(decoded_img)
    img_io.seek(0)

    response = send_file(
        img_io,
        mimetype="image/jpeg",
        download_name=f"{id}.jpeg",
        as_attachment=True,
    )

    response.headers["Access-Control-Expose-Headers"] = "Content-Disposition"
    response.headers["Content-Disposition"] = f'attachment; filename="{id}.jpeg"'

    return response
