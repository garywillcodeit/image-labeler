import io
import json
from flask import send_file
from app.utils.check_tfod_data_for_export import check_tfod_data_for_export
from app.utils.select_data_by_tag import select_data_by_tag
from app.utils.prepare_img_for_export import prepare_img_for_export
from app.utils.define_export_file_name import define_export_file_name


def export_as_json_tfod_ctrl(data):
    tags = data["tags"]

    # CHECK DATA
    check_tfod_data_for_export()

    # SELECT THE DATA
    images = select_data_by_tag(tags)

    # GET FILE NAME
    file_name = define_export_file_name()

    # PREPARE DATA FOR DOWNLOAD
    export_images = prepare_img_for_export(images)

    export_images = json.dumps(export_images, indent=1)

    io_data = io.BytesIO()

    io_data.write(export_images.encode("utf-8"))

    io_data.seek(0)

    response = send_file(
        io_data,
        mimetype="application/json",
        download_name=file_name,
    )

    response.headers["Access-Control-Expose-Headers"] = "Content-Disposition"
    response.headers["Content-Disposition"] = f"attachment; filename={file_name}"

    return response
