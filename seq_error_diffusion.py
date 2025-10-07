import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

def seq_error_diffusion(image_path, output_path, threshold=128):
    """
    Applies sequential error diffusion dithering to an image and saves the result.

    Parameters:
    - image_path: str, path to the input image.
    - output_path: str, path to save the dithered image.
    - threshold: int, threshold value for dithering (default is 128).
    """
    # Load image and convert to grayscale
    img = Image.open(image_path).convert('L')
    img_array = np.array(img)

    # Initialize output array
    dithered_img = np.zeros_like(img_array)

    # Get image dimensions
    height, width = img_array.shape

    # Sequential error diffusion
    for y in range(height):
        for x in range(width):
            old_pixel = img_array[y, x]
            new_pixel = 255 if old_pixel > threshold else 0
            dithered_img[y, x] = new_pixel
            quant_error = old_pixel - new_pixel

            # Distribute the quantization error to neighboring pixels
            if x + 1 < width:
                img_array[y, x + 1] += quant_error * 7 / 16
            if x - 1 >= 0 and y + 1 < height:
                img_array[y + 1, x - 1] += quant_error * 3 / 16
            if y + 1 < height:
                img_array[y + 1, x] += quant_error * 5 / 16
            if x + 1 < width and y + 1 < height:
                img_array[y + 1, x + 1] += quant_error * 1 / 16

    # Save the dithered image
    dithered_image = Image.fromarray(dithered_img)
    dithered_image.save(output_path)

input_image_path = 'image/grayscale_image/grayscale_airport_1024.png'  # Replace with your input image path
output_image_path = 'error_diff.png'  # Replace with your desired output image path
seq_error_diffusion(input_image_path, output_image_path)    