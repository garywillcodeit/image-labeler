def remove_unconcerned_objects(data, labelId):

    for i, e in enumerate(data):
        objects = e["selectedObjects"]
        objects = [obj for obj in objects if obj["labelId"] == labelId]

        data[i]["selectedObjects"] = objects

    return data
