import io
import os
import json
import base64
import xml.etree.ElementTree as ET
from flask import send_file
import zipfile
from app.utils.check_tfod_data_for_export import check_tfod_data_for_export
from app.utils.select_data_by_tag import select_data_by_tag
from uuid import uuid4
from app.utils.dir_path import (
    images_data_db_path,
    images_files_db_path,
    tfod_xml_template_path,
    labels_db_path,
)
from PIL import Image


def export_tfod_data_ctrl(data):
    tags = data["tags"]
    zip_buffer = io.BytesIO()

    # CHECK DATA
    check_tfod_data_for_export()

    # PREPARE DATA FOR DOWNLOAD
    image_data_list = select_data_by_tag(tags)

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:

        for img_data_name in image_data_list:
            data_path = os.path.join(images_data_db_path, img_data_name)

            with open(data_path, "r") as f:
                img_data = json.load(f)

            export_img_filename = img_data["filename"] + ".jpeg"
            export_xml_filename = img_data["filename"] + ".xml"

            with open(labels_db_path, "r") as f:
                labels = json.load(f)

            img_filename = img_data["filename"]

            img_path = os.path.join(images_files_db_path, img_filename)

            with open(img_path, "r") as f:
                img_base64 = f.read()

            decoded_img = base64.b64decode(img_base64)

            image_byte = io.BytesIO(decoded_img)

            with Image.open(image_byte) as img:
                (width, height) = img.size
                channels = len(img.mode)

            tree = ET.parse(tfod_xml_template_path)
            root = tree.getroot()

            root.find("filename").text = img_data["name"]
            root.find("size/width").text = str(width)
            root.find("size/height").text = str(height)
            root.find("size/depth").text = str(channels)

            for obj in img_data["selectedObjects"]:
                for label in labels:
                    if label["id"] == obj["labelId"]:
                        object_name = label["name"]

                object_element = ET.SubElement(root, "object")

                name_element = ET.SubElement(object_element, "name")
                name_element.text = object_name

                pose_element = ET.SubElement(object_element, "pose")
                pose_element.text = "Unspecified"

                truncated_element = ET.SubElement(object_element, "truncated")
                truncated_element.text = "Unspecified"

                difficult_element = ET.SubElement(object_element, "difficult")
                difficult_element.text = "0"

                bndbox_element = ET.SubElement(object_element, "bndbox")

                xmin = int(
                    width * obj["left"] / 100,
                )
                ymin = int(
                    height * obj["top"] / 100,
                )
                xmax = int(
                    width * (obj["left"] + obj["width"]) / 100,
                )
                ymax = int(
                    height * (obj["top"] + obj["height"]) / 100,
                )

                ET.SubElement(bndbox_element, "xmin").text = str(xmin)
                ET.SubElement(bndbox_element, "ymin").text = str(ymin)
                ET.SubElement(bndbox_element, "xmax").text = str(xmax)
                ET.SubElement(bndbox_element, "ymax").text = str(ymax)

            xml_str = ET.tostring(root, encoding="unicode")

            zipf.writestr(export_xml_filename, xml_str)
            zipf.writestr(export_img_filename, image_byte.getvalue())

    zip_buffer.seek(0)

    file_name = "tfod_data_from_img_labeler" + str(uuid4())

    response = send_file(
        zip_buffer,
        mimetype="application/zip",
        download_name=file_name,
    )

    response.headers["Access-Control-Expose-Headers"] = "Content-Disposition"
    response.headers["Content-Disposition"] = f"attachment; filename={file_name}"

    return response
