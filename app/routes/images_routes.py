from flask import Blueprint, request, jsonify
from app.controllers.images.add_image_from_device_ctrl import add_image_from_device_ctrl
from app.controllers.images.delete_image_ctrl import delete_image_ctrl
from app.controllers.images.get_image_ctrl import get_image_ctrl
from app.controllers.images.delete_all_images_ctrl import delete_all_images_ctrl
from app.controllers.images.add_selection_frame_ctrl import add_selection_frame_ctrl
from app.controllers.images.update_label_name_ctrl import update_label_name_ctrl
from app.controllers.images.delete_label_ctrl import delete_label_ctrl
from app.controllers.images.delete_all_labels_ctrl import delete_all_labels_ctrl
from app.controllers.images.video_shutter_ctrl import video_shutter_ctrl
from app.controllers.images.add_image_from_url_ctrl import add_image_from_url_ctrl
from app.controllers.images.update_selection_frame_ctrl import (
    update_selection_frame_ctrl,
)
from app.controllers.images.delete_duplicated_images_ctrl import (
    delete_duplicated_images_ctrl,
)
from app.controllers.images.get_images_count_ctrl import get_images_count_ctrl
from app.controllers.images.define_tag_color_ctrl import define_tag_color_ctrl
from app.controllers.images.rotate_image import rotate_image_ctrl
from app.controllers.images.duplicate_selection_frame_ctrl import (
    duplicate_selection_frame_ctrl,
)
from app.controllers.images.add_complete_selection_frame_ctrl import (
    add_complete_selection_frame_ctrl,
)
from app.controllers.images.get_image_by_label_id_ctrl import get_image_by_label_id_ctrl
from app.controllers.images.check_and_delete_image_ctrl import (
    check_and_delete_image_ctrl,
)


images_bp = Blueprint("images", __name__)


@images_bp.route("/add-from-device", methods=["POST"])
def add_from_device():
    return add_image_from_device_ctrl(request.files)


@images_bp.route("/add-from-url", methods=["POST"])
def add_from_url():
    data = request.get_json()
    try:
        return add_image_from_url_ctrl(data)

    except Exception as e:
        return str(e), 400


@images_bp.route("/capture-image", methods=["POST"])
def video_shutter():
    data = request.get_json()
    return video_shutter_ctrl(data)


@images_bp.route("/delete/<id>", methods=["DELETE"])
def delete_image(id):
    return delete_image_ctrl(id)


@images_bp.route("/check-and-delete/<id>", methods=["DELETE"])
def check_and_delete_image(id):
    return check_and_delete_image_ctrl(id)


@images_bp.route("/delete-all-images", methods=["DELETE"])
def delete_all_image():
    return delete_all_images_ctrl()


@images_bp.route("/find-one/<id>", methods=["GET"])
def get_image(id):
    return get_image_ctrl(id)


@images_bp.route("/get-image-by-label-id/<id>", methods=["GET"])
def get_image_by_label_id(id):
    return get_image_by_label_id_ctrl(id)


@images_bp.route("/add-selection-frame/<image_id>", methods=["POST"])
def add_selection_frame(image_id):
    data = request.get_json()
    return add_selection_frame_ctrl(image_id, data)


@images_bp.route("/add-complete-selection-frame/<image_id>")
def add_complete_selection_frame(image_id):
    return add_complete_selection_frame_ctrl(image_id)


@images_bp.route("/duplicate-selection-frame/<image_id>/<frame_id>", methods=["POST"])
def duplicate_selection_frame(image_id, frame_id):
    data = request.get_json()
    return duplicate_selection_frame_ctrl(image_id, frame_id, data)


@images_bp.route("/update-selection-frame/<image_id>/<frame_id>", methods=["POST"])
def update_selection_frame(image_id, frame_id):
    data = request.get_json()
    return update_selection_frame_ctrl(image_id, frame_id, data)


@images_bp.route("/update-label-name/<image_id>/<frame_id>", methods=["POST"])
def update_label_name(image_id, frame_id):
    data = request.get_json()
    return update_label_name_ctrl(image_id, frame_id, data)


@images_bp.route("/delete-label/<image_id>/<frame_id>", methods=["DELETE"])
def delete_label(image_id, frame_id):
    return delete_label_ctrl(image_id, frame_id)


@images_bp.route("/delete-all-labels/<image_id>", methods=["DELETE"])
def delete_all_labels(image_id):
    return delete_all_labels_ctrl(image_id)


@images_bp.route("/delete-duplicated-images")
def check_duplicate():
    try:
        return delete_duplicated_images_ctrl()

    except Exception as e:
        return jsonify(e.args[0]), 400


@images_bp.route("/get-count")
def get_images_count():
    return get_images_count_ctrl()


@images_bp.route("/update-tag-color", methods=["PUT"])
def define_tag_color():
    data = request.get_json()
    try:
        return define_tag_color_ctrl(data)

    except Exception as e:
        return jsonify(e.args[0]), 400


@images_bp.route("/rotate/<type>/<image_id>")
def turn_left(type, image_id):
    return rotate_image_ctrl(type, image_id)
