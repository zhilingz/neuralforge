"""RMSprop optimizer."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.optim.optimizer import Optimizer

__all__ = ['RMSprop']


class RMSprop(Optimizer):
    """RMSprop implementation."""

    def __init__(self, params: Any, lr: float = 0.001, alpha: float = 0.99, eps: float = 1e-8):
        self.params = params
        self.lr = lr
        self.alpha = alpha
        self.eps = eps

    def step(self, ):
        """Apply RMSprop update."""
        for p in self.params:
            pass

