from PIL import Image

def rotate_image(image_path, degrees):
    # Open the image file
    with Image.open(image_path) as img:
        # Rotate the image
        rotated_img = img.rotate(degrees)

        # Save the rotated image to a new file
        rotated_image_path = "rotated_image.png"
        rotated_img.save(rotated_image_path)

    # Return the path to the rotated image file
    return rotated_image_path