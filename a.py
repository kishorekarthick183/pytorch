import torch


# -----------------------------
# Sigmoid
# -----------------------------
def sigmoid(z):
    return 1 / (1 + torch.exp(-z))


# -----------------------------
# Binary Cross Entropy
# -----------------------------
def binary_cross_entropy(prediction, actual):
    return -(
        actual * torch.log(prediction)
        + (1 - actual) * torch.log(1 - prediction)
    ).mean()


# -----------------------------
# Dataset
# -----------------------------
X = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0],
    [6.0]
])

y = torch.tensor([
    [0.0],
    [0.0],
    [0.0],
    [1.0],
    [1.0],
    [1.0]
])


# -----------------------------
# Model parameters
# -----------------------------
w = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)

learning_rate = 0.1


# -----------------------------
# Training
# -----------------------------
for epoch in range(1000):

    # 1. Forward pass
    z = X * w + b

    prediction = sigmoid(z)

    # 2. Calculate loss
    loss = binary_cross_entropy(prediction, y)

    # 3. Calculate gradients
    loss.backward()

    # 4. Update parameters
    with torch.no_grad():
        w -= learning_rate * w.grad
        b -= learning_rate * b.grad

    # 5. Clear gradients
    w.grad.zero_()
    b.grad.zero_()

    # 6. Print progress
    if epoch % 100 == 0:
        print(
            f"Epoch {epoch:4d} | "
            f"Loss: {loss.item():.4f} | "
            f"w: {w.item():.4f} | "
            f"b: {b.item():.4f}"
        )


# -----------------------------
# Final prediction
# -----------------------------

z = X * w + b

prediction = sigmoid(z)

predicted_class = (prediction >= 0.5).float()

# -----------------------------
# Confusion Matrix
# -----------------------------

true_negative = ((y == 0) & (predicted_class == 0)).sum()

false_positive = ((y == 0) & (predicted_class == 1)).sum()

false_negative = ((y == 1) & (predicted_class == 0)).sum()

true_positive = ((y == 1) & (predicted_class == 1)).sum()


print("\n--- Confusion Matrix ---")

print("TN:", true_negative.item())
print("FP:", false_positive.item())
print("FN:", false_negative.item())
print("TP:", true_positive.item())

confusion_matrix = torch.tensor([
    [true_negative, false_positive],
    [false_negative, true_positive]
])
print(confusion_matrix)


# -----------------------------
# Accuracy
# -----------------------------

correct = (predicted_class == y).float()

accuracy = correct.mean()

# ----------------------------
# precision
# ------------------------------
precision = true_positive / (true_positive + false_positive)

print("Precision:", precision.item())

# -----------------------------
# recall
#------------------------------
recall = true_positive / (true_positive + false_negative)

print("Precision:", precision.item())
print("Recall:", recall.item())

# -----------------------------
# Decision boundary
# -----------------------------

decision_boundary = -b / w


# -----------------------------
# Results
# -----------------------------

print("\n--- Final Results ---")

print("w:", w.item())
print("b:", b.item())

print("\nProbabilities:")
print(prediction.detach().squeeze())

print("\nPredicted Classes:")
print(predicted_class.detach().squeeze())

print("\nActual Classes:")
print(y.squeeze())

print("\nCorrect:")
print(correct.squeeze())

print("\nAccuracy:", accuracy.item())

print("\nDecision Boundary:", decision_boundary.item())