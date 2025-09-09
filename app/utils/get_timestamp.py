from datetime import datetime


def get_timestamp():
    timestamp = str(datetime.timestamp(datetime.now()))
    timestamp = "".join(timestamp.split("."))
    return int(timestamp)
