import torch

x = torch.arange(6)
y = x.reshape(2, 3)
z = x.view(2, 3)
print(y, z)