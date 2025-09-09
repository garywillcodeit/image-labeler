from .get_all_images_ctrl import get_all_images_ctrl
from .get_image_ctrl import get_image_ctrl


def get_image_by_label_id_ctrl(label_id):
    images = get_all_images_ctrl()

    for img in images:
        for obj in img["selectedObjects"]:
            if obj["labelId"] == int(label_id):
                return get_image_ctrl(img["id"])

    return "No Image found", 400
