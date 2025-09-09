def is_allowed_file(filename):
    allowed_format = ["png", "jpg", "jpeg", "webp"]
    return True if filename.split(".")[-1].lower() in allowed_format else False
