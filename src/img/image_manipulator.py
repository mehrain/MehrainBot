from PIL import Image

def rotate_image(image_path, degrees):
    with Image.open(image_path) as img:
        rotated_img = img.rotate(degrees)

        rotated_image_path = "rotated_image.png"
        rotated_img.save(rotated_image_path)

    return rotated_image_path

def grayscale_image(image_path):
    with Image.open(image_path) as img:
        grayscale_img = img.convert("L")

        grayscale_image_path = "grayscaled_image.png"
        grayscale_img.save(grayscale_image_path)

    return grayscale_image_path