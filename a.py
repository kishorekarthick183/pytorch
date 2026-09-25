import torch

X = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0]
])

y = torch.tensor([
    [3.0],
    [5.0],
    [7.0],
    [9.0],
    [11.0]
])

w = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)

learning_rate = 0.01

for epoch in range(1):

    # Forward
    prediction = w * X + b

    # Loss
    loss = ((prediction - y) ** 2).mean()

    # Backward
    loss.backward()

    print("prediction:\n", prediction)
    print("loss:", loss.item())
    print("w gradient:", w.grad.item())
    print("b gradient:", b.grad.item())

    # Update
    with torch.no_grad():
        w -= learning_rate * w.grad
        b -= learning_rate * b.grad

    # Reset gradients
    w.grad.zero_()
    b.grad.zero_()

    # Print every 100 epochs
    if epoch % 100 == 0:
        print(
            f"epoch={epoch}, "
            f"loss={loss.item():.4f}, "
            f"w={w.item():.4f}, "
            f"b={b.item():.4f}"
        )

# explain the process of chaining the loss function wrt w and b ? 