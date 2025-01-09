print("this is a trial file")
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

# Generate 1D data from a cubic function
def cubic_function(x):
    return x**3 - 6*x**2 + 4*x + 12

# Generate training data
x_train = np.linspace(-2, 5, 100).reshape(-1, 1).astype(np.float32)
y_train = cubic_function(x_train).astype(np.float32)

# Convert to PyTorch tensors
x_train_tensor = torch.tensor(x_train)
y_train_tensor = torch.tensor(y_train)

# Define the neural network class
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.hidden = nn.Linear(1, 7)
        self.activation = nn.ReLU()
        self.output = nn.Linear(7, 1)

    def forward(self, x):
        x = self.activation(self.hidden(x))
        x = self.output(x)
        return x

# Initialize the neural network, loss function, and optimizer
model = SimpleNN()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.03)

# Training the model
num_epochs = 200

for epoch in range(num_epochs):
    # Forward pass
    y_pred = model(x_train_tensor)
    loss = criterion(y_pred, y_train_tensor)

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Save the predicted curve after each epoch for visualization
    with torch.no_grad():
        if (epoch + 1) % 10 == 0:
            predicted_curve = model(x_train_tensor).numpy()

            # Plot for the current epoch
            plt.figure(figsize=(6, 4))
            plt.plot(x_train, predicted_curve, label=f"Epoch {epoch + 1}")

            # Plot the original cubic function
            y_true = cubic_function(x_train)
            plt.plot(x_train, y_true, 'k--', label="True Function")

            plt.title(f"Function Approximation at Epoch {epoch + 1}")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.legend()
            plt.grid()
            plt.show()

    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}")
