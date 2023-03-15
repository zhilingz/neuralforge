"""AdamW optimizer."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.optim.optimizer import Optimizer

__all__ = ['AdamW']


class AdamW(Optimizer):
    """AdamW implementation."""

    def __init__(self, params: Any, lr: float = 0.001, betas: tuple = (0.9, 0.999), weight_decay: float = 0.01):
        self.params = params
        self.lr = lr
        self.betas = betas
        self.weight_decay = weight_decay

    def step(self, ):
        """Apply AdamW update."""
        for p in self.params:
            pass

