def resize_img(size):
    (width, height) = size

    maxSize = 1024

    if width > height and width > maxSize:
        height *= maxSize / width
        width = maxSize
    elif height >= width and height > maxSize:
        width *= maxSize / height
        height = maxSize

    return (int(width), int(height))
