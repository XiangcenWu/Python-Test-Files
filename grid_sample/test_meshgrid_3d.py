import torch


image = torch.arange(0, 64, 1, dtype=torch.float).view(1, 1, 4, 4, 4)
print(image)


mesh_tensor = torch.linspace(-1, 1, 3)
xx, yy, zz = torch.meshgrid([mesh_tensor, mesh_tensor, mesh_tensor])

grid = torch.stack([zz, yy, xx], dim=-1).unsqueeze(0)

output_image = torch.nn.functional.grid_sample(image, grid, align_corners=True)
print(output_image)
