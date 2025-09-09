import json


def is_json_file(file_path: str) -> bool:
    try:
        with open(
            file_path,
            "r",
        ) as f:
            return json.load(f)

    except (json.JSONDecodeError, FileNotFoundError, OSError) as e:
        return False
