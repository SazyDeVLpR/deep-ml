import numpy as np

def train(X, y, W, b):
    """
    Train linear regression weights on standardized data.
    
    Args:
        X: numpy array of shape (n_samples, n_features) -- standardized features
        y: numpy array of shape (n_samples,) -- standardized targets
        W: numpy array of shape (n_features,) -- initial random weights
        b: float -- initial bias (0.0)
    
    Returns:
        W: numpy array of shape (n_features,) -- trained weights
        b: float -- trained bias
    """
    # TODO: implement your training strategy here
    # You can use ANY approach: gradient descent, normal equation,
    # momentum, adaptive learning rates, mini-batching, etc.


    learning_rate = 0.01
    epochs = 1000

    n = X.shape[0]

    for epoch in range(epochs):

        # Forward pass
        y_pred = X @ W + b

        # Error
        error = y_pred - y

        # Gradients
        dW = (2 / n) * (X.T @ error)
        db = (2 / n) * np.sum(error)

        # Gradient descent
        W = W - learning_rate * dW
        b = b - learning_rate * db

    return W, b


