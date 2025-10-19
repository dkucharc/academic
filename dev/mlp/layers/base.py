from abc import ABC

import numpy as np

class BaseLayer(ABC):
    """Base class for neural network layers."""

    def forward(self, inputs: np.ndarray) -> np.ndarray:
        raise NotImplementedError

    def backward(self, grad: np.ndarray) -> np.ndarray:
        raise NotImplementedError

    def update(self, learning_rate: float) -> None:
        pass
