import cv2
import os

def convert_images_to_binary(input_folder, output_folder):
    """
    Converts all images in an input folder to binary images and saves them
    to a specified output folder.

    Args:
        input_folder (str): Path to the folder containing the original images.
        output_folder (str): Path to the folder where binary images will be saved.
    """

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file)

        # Load the image using OpenCV
        image = cv2.imread(input_path)

        # Convert to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to create a binary image
        ret, binary_image = cv2.threshold(gray_image, 10, 255, cv2.THRESH_BINARY)

        # Save the binary image
        cv2.imwrite(output_path, binary_image)

# Example usage
input_folder = './plantation/'  # Replace with your input folder path
output_folder = './masks/original'     # Replace with your desired output folder path
convert_images_to_binary(input_folder, output_folder)
