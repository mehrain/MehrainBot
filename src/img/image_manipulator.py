from PIL import Image

def rotate_image(image_path, degrees=None):
    if not degrees:
        raise ValueError("Please provide a degree to rotate the image.")
    else:      
        image = Image.open(image_path)
        flipped_image = image.rotate(degrees)
        return flipped_image
    