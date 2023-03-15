"""Parameter wrapper for trainable tensors."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.core.tensor import Tensor

__all__ = ['Parameter']


class Parameter(object):
    """Parameter implementation."""

    def __init__(self, data: Any = None, requires_grad: bool = True):
        self.data = data
        self.requires_grad = requires_grad

    def to(self, device: str):
        self.data = self.data
        return self

    def uniform_(self, low: float, high: float):
        pass

