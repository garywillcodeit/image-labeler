import json
from app.utils.dir_path import labels_db_path, images_data_db_path
from app.utils.is_json import is_json_file
from pathlib import Path


def delete_label_ctrl(id):
    try:
        storage_list = [p for p in Path(images_data_db_path).iterdir() if p.is_file()]

        for file_path in storage_list:
            data = is_json_file(file_path)

            for ind_obj, obj in enumerate(data["selectedObjects"]):
                if obj["labelId"] == int(id):
                    raise Exception("This label is currently used with images.")

        with open(labels_db_path, "r") as f:
            labels = json.load(f)

        if len(labels) == 0:
            raise Exception("There is no label in the map.")

        for i, label in enumerate(labels):
            if label["id"] == int(id):
                labels[i] = None
                break

        labels = [lab for lab in labels if lab != None]

        for i, label in enumerate(labels):
            labels[i]["id"] = i + 1

        for file_path in storage_list:
            data = is_json_file(file_path)

            if data:

                for ind_obj, obj in enumerate(data["selectedObjects"]):

                    new_label = next(
                        label for label in labels if label["name"] == obj["labelName"]
                    )

                    data["selectedObjects"][ind_obj]["labelId"] = new_label["id"]
                    data["selectedObjects"][ind_obj]["labelName"] = new_label["name"]

                with open(file_path, "w") as f:
                    json.dump(data, f, indent=1)

        with open(labels_db_path, "w") as f:
            json.dump(labels, f, indent=1)

        return {"msg": "Label successfully deleted!"}
    except Exception as e:
        return {"msg": str(e)}, 400
