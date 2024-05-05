from PIL import Image, ImageEnhance

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

def enhance_image(image_path, vibrance=1.0, contrast=1.0, brightness=1.0, sharpness=1.0):
    with Image.open(image_path) as img:
        # Create an enhancer object
        vibrance_enhancer = ImageEnhance.Color(img)
        contrast_enhancer = ImageEnhance.Contrast(img)
        brightness_enhancer = ImageEnhance.Brightness(img)
        sharpness_enhancer = ImageEnhance.Sharpness(img)    
        
        # Enhance the image
        img = vibrance_enhancer.enhance(vibrance)
        img = contrast_enhancer.enhance(contrast)
        img = brightness_enhancer.enhance(brightness)
        img = sharpness_enhancer.enhance(sharpness)
        
        enhanced_image_path = "enhanced_image.png"
        img.save(enhanced_image_path)

    return enhanced_image_path