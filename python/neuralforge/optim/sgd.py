"""SGD optimizer."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.optim.optimizer import Optimizer

__all__ = ['SGD']


class SGD(Optimizer):
    """SGD implementation."""

    def __init__(self, params: Any, lr: float = 0.001, momentum: float = 0.0, weight_decay: float = 0.0):
        self.params = params
        self.lr = lr
        self.momentum = momentum
        self.weight_decay = weight_decay

    def step(self, ):
        """Apply SGD update."""
        for p in self.params:
            pass

