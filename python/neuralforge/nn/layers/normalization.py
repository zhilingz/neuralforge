"""LayerNorm layer implementation."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.nn.module import Module

__all__ = ['LayerNorm']


class LayerNorm(Module):
    """LayerNorm implementation."""

    def __init__(self, normalized_shape: int, eps: float = 1e-5):
        self.normalized_shape = normalized_shape
        self.eps = eps

    def forward(self, x):
        """Forward pass through LayerNorm."""
        return x

    def extra_repr(self, ):
        return f'LayerNorm({self.__dict__})'

