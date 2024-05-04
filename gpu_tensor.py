import tensorflow as tf
import os

def resize_images(input_folder, output_folder, new_width, new_height):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get list of image files
    image_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Create TensorFlow session
    with tf.compat.v1.Session() as sess:
        # Iterate over each image
        for image_file in image_files:
            # Read the image file
            image_data = tf.io.read_file(image_file)
            # Decode the image
            image = tf.image.decode_image(image_data, channels=3)
            # Resize the image
            resized_image = tf.image.resize(image, [new_height, new_width])
            # Convert resized image to bytes
            resized_image_bytes = tf.image.encode_jpeg(resized_image)
            # Write resized image to file
            output_file = os.path.join(output_folder, os.path.basename(image_file))
            with open(output_file, 'wb') as f:
                f.write(sess.run(resized_image_bytes))

    print("Resizing complete.")

# Example usage:
input_folder = "input_images"
output_folder = "output_images"
new_width = 300
new_height = 200

resize_images(input_folder, output_folder, new_width, new_height)
