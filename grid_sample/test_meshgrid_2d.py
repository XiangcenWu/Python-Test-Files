import torch


image = torch.arange(0, 16, 1, dtype=torch.float).view(1, 1, 4, 4)
print(image)

num = 3
x = torch.linspace(-1, 1, num )
y = torch.linspace(-0.9, 0.9, num)


xx, yy = torch.meshgrid([x, y])

grid = torch.stack([yy, xx], dim=-1).unsqueeze(0)
print(grid)


output_image = torch.nn.functional.grid_sample(image, grid, align_corners=True)
print(output_image)