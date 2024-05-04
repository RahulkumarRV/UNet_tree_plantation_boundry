import os
import random
import cv2
from PIL import Image

def rotate_and_select_images(image_folder, mask_folder, output_image_folder, output_mask_folder, flip_directions):
    """
    Rotates images from two input folders to specified degrees, selects a random
    subset, and saves them to corresponding output folders.

    Args:
        image_folder (str): Path to the folder containing original images.
        mask_folder (str): Path to the folder containing corresponding mask images.
        output_image_folder (str): Path to the output folder for rotated images.
        output_mask_folder (str): Path to the output folder for rotated masks.
        flip_directions (list): A list of flip_direction angles in degrees.
    """
    os.makedirs(output_image_folder, exist_ok=True)
    os.makedirs(output_mask_folder, exist_ok=True)

    num_images_per_flip_direction = 20

    image_names = os.listdir(image_folder)

    flip_names = ["vertically", "horizontally", "both"]

    for flip_direction in flip_directions:
        for _ in range(num_images_per_flip_direction):
            image_name = random.choice(image_names)
            image_path = os.path.join(image_folder, image_name)
            mask_path = os.path.join(mask_folder, image_name)

            # Load image and mask (using your preferred library)
            image = cv2.imread(image_path)  
            mask = cv2.imread(mask_path)    # PIL

            flip_image = cv2.flip(image, flip_direction)

            # Rotate mask (Pillow)
            flip_mask = cv2.flip(mask, flip_direction) 

            # Save rotated images
            out_image_path = os.path.join(output_image_folder, f"{flip_names[flip_direction + 1]}_{image_name}.png")
            out_mask_path = os.path.join(output_mask_folder, f"{flip_names[flip_direction + 1]}_{image_name}.png")
            cv2.imwrite(out_image_path, flip_image)
            cv2.imwrite(out_mask_path, flip_mask)

if __name__ == "__main__":
    image_folder = "plantation_images/images"
    mask_folder = "masks/original"
    output_image_folder = "plantation_images/fliped_images"
    output_mask_folder = "masks/fliped_masks"
    flip_directions = [0, 1, -1]

    rotate_and_select_images(image_folder, mask_folder, output_image_folder, output_mask_folder, flip_directions)
