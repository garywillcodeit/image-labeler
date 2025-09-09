from flask import Blueprint, request
from ..controllers.labels.add_new_label_ctrl import add_new_label
from ..controllers.labels.edit_label_name import edit_label_name_ctrl
from ..controllers.labels.get_all_labels import get_all_labels
from ..controllers.labels.delete_label_ctrl import delete_label_ctrl
from ..controllers.labels.get_label_ctrl import get_label_ctrl
from ..controllers.labels.define_default_label_ctrl import define_default_label_ctrl


labels_bp = Blueprint("labels", __name__)


@labels_bp.route("/add", methods=["POST"])
def add_label():
    try:
        data = request.get_json()
        return add_new_label(data)

    except Exception as e:
        return str(e), 404


@labels_bp.route("/edit/<id>", methods=["PUT"])
def edit_label(id):
    try:
        data = request.get_json()
        return edit_label_name_ctrl(id, data)

    except Exception as e:
        return str(e), 404


@labels_bp.route("/get-all", methods=["GET"])
def get_all():
    try:
        return get_all_labels()

    except Exception as e:
        return str(e), 404


@labels_bp.route("/<id>", methods=["GET"])
def get_label(id):
    return get_label_ctrl(id)


@labels_bp.route("/<id>", methods=["DELETE"])
def delete(id):
    return delete_label_ctrl(id)


@labels_bp.route("/define-default", methods=["PUT"])
def define_default():
    data = request.get_json()
    return define_default_label_ctrl(data)
