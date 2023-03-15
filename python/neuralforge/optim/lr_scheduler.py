"""Learning rate scheduler."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['StepLR']


class StepLR(object):
    """StepLR implementation."""

    def __init__(self, optimizer: Any, step_size: int = 10, gamma: float = 0.1):
        self.optimizer = optimizer
        self.step_size = step_size
        self.gamma = gamma

    def step(self, ):
        """Update learning rate."""
        self.optimizer.lr *= self.gamma

