import os
import json
import base64
import io
from multiprocessing import Pool, cpu_count
from PIL import Image, ImageChops
from app.utils.dir_path import images_data_db_path, images_files_db_path
from app.utils.get_image_file import get_image_file
from app import socketio
from app.controllers.load_init_data import load_init_data
from tqdm import tqdm


def delete_duplicated_images_ctrl(logs=False):

    deleted_images = 0
    last_progress_msg = None

    images = os.listdir(images_data_db_path)

    cpu = cpu_count()
    nb_process = max(1, cpu // 2)

    with Pool(processes=nb_process) as pool:
        for i, _ in tqdm(
            enumerate(pool.imap_unordered(process, images)),
            total=len(images),
            desc="Processing",
            unit="images",
        ):
            progress = f"{int((i + 1) / len(images) * 100)}%"

            if last_progress_msg != progress:
                last_progress_msg = progress

                if logs:
                    print(progress)
                else:
                    socketio.emit(
                        "message",
                        {"data": f"Looking for duplicate images... {progress}"},
                    )

    data = load_init_data()
    data["msg"] = (
        f"{deleted_images} duplicated image{deleted_images > 1 and 's'} successfully deleted!"
    )
    return data


def process(img1):
    first_img = get_image_byte(img1)

    if first_img != None:
        images = os.listdir(images_data_db_path)

        for i, img2 in enumerate(images):
            if img1 and img2 and img1 != img2:
                second_img = get_image_byte(img2)

                if second_img:
                    result = are_identical(first_img, second_img)

                    if result:
                        img_data = get_image_data(img2)
                        if img_data:
                            data_path = os.path.join(images_data_db_path, img2)
                            file_path = os.path.join(
                                images_files_db_path, img_data["filename"]
                            )

                            os.remove(data_path)
                            os.remove(file_path)
                            images[i] = None


def are_identical(first_img, second_img):
    try:
        img1 = Image.open(first_img)
        img2 = Image.open(second_img)

        diff = ImageChops.difference(img1, img2)

        if diff.getbbox() is None:
            return True
        else:
            return False
    except:
        return False


def get_image_byte(img):

    if img != None:
        data = get_image_data(img)

        if data:
            image = get_image_file(data["filename"])
            image = image.split(",")[1]
            image = base64.b64decode(image)
            image = io.BytesIO(image)

            return image
        else:
            return None
    else:
        return None


def get_image_data(img):
    path = os.path.join(images_data_db_path, img)
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    else:
        return None
