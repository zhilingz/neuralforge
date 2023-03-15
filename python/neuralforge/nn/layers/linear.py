"""Linear layer implementation."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.nn.module import Module

__all__ = ['Linear']


class Linear(Module):
    """Linear implementation."""

    def __init__(self, in_features: int, out_features: int, bias: bool = True):
        self.in_features = in_features
        self.out_features = out_features
        self.bias = bias

    def forward(self, x):
        """Forward pass through Linear."""
        return x

    def extra_repr(self, ):
        return f'Linear({self.__dict__})'

