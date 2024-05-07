import os
from PIL import Image
from torch.utils.data import Dataset

class CustomDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.image_files = os.listdir(os.path.join(root_dir, "image/test"))
        self.mask_files = os.listdir(os.path.join(root_dir, "mask/test"))

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        image_name = self.image_files[idx]
        mask_name = self.mask_files[idx]

        image_path = os.path.join(self.root_dir, "image/test", image_name)
        mask_path = os.path.join(self.root_dir, "mask/test", mask_name)

        image = Image.open(image_path)
        mask = Image.open(mask_path)

        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        if self.transform:
            image = self.transform(image)
            mask = self.transform(mask)

        return image, mask
