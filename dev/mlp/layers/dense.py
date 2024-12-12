import numpy as np

from dev.mlp.layers.base import BaseLayer


class DenseLayer(BaseLayer):
    """Fully connected layer."""

    def __init__(self, input_dim: int, output_dim: int):

        self.weights = np.random.randn(input_dim, output_dim) * np.sqrt(2 / input_dim)
        self.biases = np.zeros((1, output_dim))
        self.inputs = None
        self.grad_weights = None
        self.grad_biases = None

    def forward(self, inputs: np.ndarray) -> np.ndarray:
        self.inputs = inputs
        return np.dot(inputs, self.weights) + self.biases

    def backward(self, grad: np.ndarray) -> np.ndarray:
        self.grad_weights = np.dot(self.inputs.T, grad)
        self.grad_biases = np.sum(grad, axis=0, keepdims=True)
        return np.dot(grad, self.weights.T)

    def update(self, learning_rate: float) -> None:
        self.weights -= learning_rate * self.grad_weights
        self.biases -= learning_rate * self.grad_biases
