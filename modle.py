# # prompt: create a unet modle

# import torch
# import torch.nn as nn

# class Downsample(nn.Module):
#   def __init__(self, in_channels, out_channels, kernel_size=3):
#     super(Downsample, self).__init__()
#     self.conv = nn.Sequential(
#       nn.Conv2d(in_channels, out_channels, kernel_size, padding="same"),
#       nn.ReLU(inplace=True),
#       nn.BatchNorm2d(out_channels),
#       nn.Conv2d(out_channels, out_channels, kernel_size, padding="same"),
#       nn.ReLU(inplace=True),
#       nn.BatchNorm2d(out_channels),
#     )
#     self.pool = nn.MaxPool2d(2, 2)

#   def forward(self, x, is_pool):
#     out = self.conv(x)
#     if is_pool:
#       out = self.pool(out)
#     return out

# class Upsample(nn.Module):
#   def __init__(self, in_channels):
#     super(Upsample, self).__init__()
#     self.up = nn.ConvTranspose2d(
#       in_channels, in_channels // 2, kernel_size=2, stride=2
#     )
#     self.conv = Downsample(in_channels, in_channels // 2)

#   def forward(self, x1, x2):
#     x1 = self.up(x1)
#     diffY = x2.size()[2] - x1.size()[2]
#     diffX = x2.size()[3] - x1.size()[3]
#     x1 = nn.functional.pad(x1, [diffX // 2, diffX - diffX // 2, diffY // 2, diffY - diffY // 2])
#     out = torch.cat([x2, x1], dim=1)
#     out = self.conv(out)
#     return out

# class Unet(nn.Module):
#   def __init__(self):
#     super(Unet, self).__init__()
#     self.down1 = Downsample(1, 64)
#     self.down2 = Downsample(64, 128)
#     self.down3 = Downsample(128, 256)
#     self.down4 = Downsample(256, 512)
#     self.down5 = Downsample(512, 1024)

#     self.up = nn.ConvTranspose2d(1024, 512, kernel_size=3, stride=2, padding=1, output_padding=1)
#     self.up1 = Upsample(512)
#     self.up2 = Upsample(256)
#     self.up3 = Upsample(128)
#     self.conv_4 = Downsample(128, 64)

#     self.last = nn.Conv2d(64, 2, kernel_size=1)

#   def forward(self, x):
#     x1 = self.down1(x, is_pool=False)
#     x2 = self.down2(x1)
#     x3 = self.down3(x2)
#     x4 = self.down4(x3)
#     x5 = self.down5(x4)

#     x5 = self.up(x5)
#     x5 = torch.cat([x4, x5], dim=1)
#     x5 = self.up1(x5)
#     x5 = torch.cat([x3, x5], dim=1)
#     x5 = self.up2(x5)
#     x5 = torch.cat([x2, x5], dim=1)
#     x5 = self.up3(x5)
#     x5 = torch.cat([x1, x5], dim=1)
#     x5 = self.conv_4(x5, is_pool=False)
#     x5 = self.last(x5)
#     return x5

import matplotlib.pyplot as plt
import os
from PIL import Image

# Folder path containing the images
folder_path = './temp'

# List to store images
images = []

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Read the image using PIL
        image = Image.open(os.path.join(folder_path, filename))
        # Append the image to the list
        images.append(image)

# Create a figure and axis array with 4 rows and 3 columns
fig, axs = plt.subplots(4, 3, figsize=(12, 12))

# Plot each image in a subplot
for i in range(4):
    for j in range(3):
        ax = axs[i, j]
        # Check if there are remaining images to plot
        index = i * 3 + j
        if index < len(images):
            ax.imshow(images[index])  # Display the image
            ax.axis('off')  # Turn off axis
        else:
            ax.axis('off')  # Turn off axis if no image to plot

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
