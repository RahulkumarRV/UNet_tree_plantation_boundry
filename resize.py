import os
import sys
from PIL import Image

def resize_images(folder_path):
    """
    Resizes all images in a folder to 1024x1024 and saves them in the same folder.

    Args:
        folder_path (str): Path to the folder containing the images.
    """

    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            try:
                image_path = os.path.join(folder_path, filename)
                img = Image.open(image_path)
                resized_img = img.resize((2048, 2048), Image.Resampling.LANCZOS)

                resized_img.save(image_path, quality=95)  # Save with high quality
                print(f"{filename} resized successfully.")
            except Exception as e:
                print(f"Error processing {filename}: {e}") 

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python resize_images.py <folder_path>")
    else:
        folder_path = sys.argv[1]
        resize_images(folder_path)
