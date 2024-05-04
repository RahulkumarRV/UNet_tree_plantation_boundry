import os
import random
import shutil

def partition_data(images_dir, masks_dir, output_dir, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15):
    # Create output directories
    output_image_dir = os.path.join(output_dir, "image")
    train_dir = os.path.join(output_image_dir, "train")
    val_dir = os.path.join(output_image_dir, "val")
    test_dir = os.path.join(output_image_dir, "test")

    output_mask_dir = os.path.join(output_dir, "mask")
    train_mask_dir = os.path.join(output_mask_dir, "train")
    val_mask_dir = os.path.join(output_mask_dir, "val")
    test_mask_dir = os.path.join(output_mask_dir, "test")

    for dir_path in [train_dir, val_dir, test_dir, train_mask_dir, val_mask_dir, test_mask_dir]:
        os.makedirs(dir_path, exist_ok=True)

    # Get list of image files
    image_files = sorted([f for f in os.listdir(images_dir) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))])

    # Randomly shuffle the images
    random.seed(42)  # For reproducibility
    random.shuffle(image_files)

    # Calculate split indices
    num_images = len(image_files)
    num_train = int(train_ratio * num_images)
    num_val = int(val_ratio * num_images)

    # Split image files
    train_images = image_files[:num_train]
    val_images = image_files[num_train:num_train+num_val]
    test_images = image_files[num_train+num_val:]

    # Copy images to their respective directories
    for image in train_images:
        shutil.copy(os.path.join(images_dir, image), os.path.join(train_dir, image))
        shutil.copy(os.path.join(masks_dir, image), os.path.join(train_mask_dir, image))
    for image in val_images:
        shutil.copy(os.path.join(images_dir, image), os.path.join(val_dir, image))
        shutil.copy(os.path.join(masks_dir, image), os.path.join(val_mask_dir, image))
    for image in test_images:
        shutil.copy(os.path.join(images_dir, image), os.path.join(test_dir, image))
        shutil.copy(os.path.join(masks_dir, image), os.path.join(test_mask_dir, image))

    print("Partitioning complete.")

# Example usage:
images_dir = ["images/images", "images/fliped_images", "images/rotated_images"]
masks_dir = ["masks/masks", "masks/fliped_masks", "masks/rotated_masks"]
output_dir = "data_partitioned"

for i in range(len(images_dir)):
    partition_data(images_dir[i], masks_dir[i], output_dir)
