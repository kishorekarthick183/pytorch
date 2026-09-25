import torch

w = torch.tensor(2.0, requires_grad=True)

x = torch.tensor(3.0)
actual = torch.tensor(10.0)

learning_rate = 0.01

for i in range(1000):
    # Forward
    prediction = w * x

    # Loss
    loss = (prediction - actual) ** 2

    # Gradient
    loss.backward()

    print(
        "iteration:", i,
        "w:", w.item(),
        "prediction:", prediction.item(),
        "loss:", loss.item(),
        "gradient:", w.grad.item()
    )

    # Update
    with torch.no_grad():
        w -= learning_rate * w.grad

    w.grad.zero_()

# actual vs predicted. 
# let actual be  10. then predict = 2 * 3 = 6
# loss = (4) ** 2 = 16. let loss = 16 then when 
# loss.backward() is mean is dL / dw = can be calculated by gradient. isn't it ? 
# w is before item. before the input is 2 in w.item(). then we have updated to 
# w -= rate * grad. 
# yep make tthe weight to change so to better results in the actual output. 
# lets make it obvious. when 2 * 3 we get 6. when we want 10 then we can make the 2 to be increased 
# rigth ? so w.item willllll resultss in After: 2.240000009536743
# thus we have increased the w by iterating single time so we can achieve the actual value
# 