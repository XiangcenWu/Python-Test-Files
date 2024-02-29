import torch
from load_image import load_image
import matplotlib.pyplot as plt
import numpy as np
import nibabel as nib
# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

img = load_image(r'C:\Users\Xiangcen\Desktop\Python Test File\grid_sample\data\001000_img.nii').unsqueeze(0).unsqueeze(0).float()
ax1.imshow(img[0, 0, :, :, 9])

x_mesh_tensor = torch.linspace(-1, 1, 180)
y_mesh_tensor = torch.linspace(-1, 1, 180)
z_mesh_tensor = torch.linspace(-1, 1, 36)


xx, yy, zz = torch.meshgrid([x_mesh_tensor, y_mesh_tensor, z_mesh_tensor])
grid = torch.stack([zz, yy, xx], dim=-1).unsqueeze(0).float()


output_image = torch.nn.functional.grid_sample(img, grid, align_corners=True).squeeze(0).squeeze(0)
ax2.imshow(output_image[:, :, 9])
print(output_image.shape)
output_image = np.array(output_image)
output_img = nib.Nifti1Image(output_image, affine=np.eye(4))

nib.save(output_img, r'C:\Users\Xiangcen\Desktop\Python Test File\grid_sample\processed_data\output_file.nii')

plt.show()
