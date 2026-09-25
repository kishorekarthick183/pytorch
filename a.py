import torch

w = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)
x = torch.tensor(3.0)

actual = torch.tensor(7.0)

learning_rate = 0.01
prediction = w * x + b
print("prediction ", prediction)

# Loss
loss = (prediction - actual) ** 2

print(loss) # (7 - (0 * 3 + 0))^2 -> 49.

# Gradient
loss.backward()

print(w.grad) # -42
print(b.grad) # -14

# Update
with torch.no_grad():
    w -= learning_rate * w.grad
    b -= learning_rate * b.grad
    print(w) # 0.42
    print(b) # 0.14
    print("prediction new ", w * x+ b)