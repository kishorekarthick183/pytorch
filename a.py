import torch

# Dummy model weights
w = torch.tensor([1.5], requires_grad=True)
b = torch.tensor([0.5], requires_grad=True)

test_x = torch.tensor([2.0, 4.0, 6.0])

# Disable gradient tracking for inference
with torch.no_grad():
    predictions = test_x * w + b

print(predictions)
print(predictions.requires_grad)  # Output: False