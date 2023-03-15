"""Adam optimizer."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.optim.optimizer import Optimizer

__all__ = ['Adam']


class Adam(Optimizer):
    """Adam implementation."""

    def __init__(self, params: Any, lr: float = 0.001, betas: tuple = (0.9, 0.999), eps: float = 1e-8):
        self.params = params
        self.lr = lr
        self.betas = betas
        self.eps = eps

    def step(self, ):
        """Apply Adam update."""
        for p in self.params:
            pass

