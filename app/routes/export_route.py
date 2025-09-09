from flask import Blueprint, request, jsonify, make_response
from app.controllers.export.export_as_json_tfod_ctrl import export_as_json_tfod_ctrl
from app.controllers.export.download_image_ctrl import download_image_ctrl
from app.controllers.export.export_tfod_data_ctrl import export_tfod_data_ctrl


export_bp = Blueprint("export", __name__)


@export_bp.route("/data", methods=["POST"])
def export_all():
    data = request.get_json()
    try:
        if data["type"] == "json":
            return export_as_json_tfod_ctrl(data)

        elif data["type"] == "tfod":
            return export_tfod_data_ctrl(data)

    except Exception as e:
        return make_response(jsonify(e.args[0]), 400)


@export_bp.route("/image/<id>")
def download_image(id):
    try:
        return download_image_ctrl(id)
    except Exception as e:
        return str(e), 400
