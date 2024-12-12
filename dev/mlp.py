from typing import List, Union, Callable, Optional, Dict, Type
import numpy as np





class Activation(Layer):
    """Base class for activation layers."""

    def __init__(self):
        self.inputs = None


class ReLU(Activation):
    def forward(self, inputs: np.ndarray) -> np.ndarray:
        self.inputs = inputs
        return np.maximum(0, inputs)

    def backward(self, grad: np.ndarray) -> np.ndarray:
        return grad * (self.inputs > 0)


class Sigmoid(Activation):
    def forward(self, inputs: np.ndarray) -> np.ndarray:
        self.inputs = inputs
        return 1 / (1 + np.exp(-inputs))

    def backward(self, grad: np.ndarray) -> np.ndarray:
        s = self.forward(self.inputs)
        return grad * s * (1 - s)


class MLP:
    """Generic Multilayer Perceptron implementation."""

    def __init__(self, random_state: Optional[int] = None):
        if random_state is not None:
            np.random.seed(random_state)
        self.layers: List[Layer] = []

    def add(self, layer: Layer) -> None:
        """Add a layer to the network."""
        self.layers.append(layer)

    def forward(self, X: np.ndarray) -> np.ndarray:
        """Forward pass through all layers."""
        output = X
        for layer in self.layers:
            output = layer.forward(output)
        return output

    def backward(self, grad: np.ndarray) -> None:
        """Backward pass through all layers."""
        for layer in reversed(self.layers):
            grad = layer.backward(grad)

    def update(self, learning_rate: float) -> None:
        """Update all layer parameters."""
        for layer in self.layers:
            layer.update(learning_rate)

    def fit(
            self,
            X: np.ndarray,
            y: np.ndarray,
            epochs: int = 1000,
            batch_size: int = 32,
            learning_rate: float = 0.1,
            verbose: bool = False
    ) -> None:
        """Train the neural network."""
        m = X.shape[0]

        for epoch in range(epochs):
            for i in range(0, m, batch_size):
                batch_X = X[i:i + batch_size]
                batch_y = y[i:i + batch_size]

                # Forward pass
                predictions = self.forward(batch_X)

                # Compute gradient of loss
                grad = predictions - batch_y

                # Backward pass
                self.backward(grad)

                # Update parameters
                self.update(learning_rate)

            if verbose and epoch % 100 == 0:
                predictions = self.forward(X)
                mse = np.mean((predictions - y) ** 2)
                print(f"Epoch {epoch}: MSE = {mse:.4f}")

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict class labels for input samples."""
        return np.argmax(self.forward(X), axis=1)