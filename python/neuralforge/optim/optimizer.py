"""Base optimizer."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['Optimizer']


class Optimizer(object):
    """Optimizer implementation."""

    def __init__(self, params: Any, lr: float = 0.001):
        self.params = params
        self.lr = lr

    def step(self, ):
        """Perform optimization step."""
        raise NotImplementedError

    def zero_grad(self, ):
        """Zero all gradients."""
        pass

