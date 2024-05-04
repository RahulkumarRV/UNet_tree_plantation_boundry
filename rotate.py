import os
import random
import cv2
from PIL import Image

def rotate_and_select_images(image_folder, mask_folder, output_image_folder, output_mask_folder, rotations):
    """
    Rotates images from two input folders to specified degrees, selects a random
    subset, and saves them to corresponding output folders.

    Args:
        image_folder (str): Path to the folder containing original images.
        mask_folder (str): Path to the folder containing corresponding mask images.
        output_image_folder (str): Path to the output folder for rotated images.
        output_mask_folder (str): Path to the output folder for rotated masks.
        rotations (list): A list of rotation angles in degrees.
    """
    os.makedirs(output_image_folder, exist_ok=True)
    os.makedirs(output_mask_folder, exist_ok=True)

    num_images_per_rotation = 20

    image_names = os.listdir(image_folder)

    for rotation in rotations:
        for _ in range(num_images_per_rotation):
            image_name = random.choice(image_names)
            image_path = os.path.join(image_folder, image_name)
            mask_path = os.path.join(mask_folder, image_name)

            # Load image and mask (using your preferred library)
            image = Image.open(image_path)  
            mask = Image.open(mask_path)    # PIL

            rotated_image = image.rotate(rotation)

            # Rotate mask (Pillow)
            rotated_mask = mask.rotate(rotation) 

            # Save rotated images
            out_image_path = os.path.join(output_image_folder, f"{rotation}_{image_name}")
            out_mask_path = os.path.join(output_mask_folder, f"{rotation}_{image_name}")
            rotated_image.save(out_image_path)
            rotated_mask.save(out_mask_path)

if __name__ == "__main__":
    image_folder = "plantation_images/images"
    mask_folder = "masks/original"
    output_image_folder = "plantation_images/rotated_images"
    output_mask_folder = "masks/rotated_masks"
    rotations = [45, 60, 120, 165, 210]

    rotate_and_select_images(image_folder, mask_folder, output_image_folder, output_mask_folder, rotations)
