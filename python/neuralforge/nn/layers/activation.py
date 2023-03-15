"""ReLU layer implementation."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.nn.module import Module

__all__ = ['ReLU']


class ReLU(Module):
    """ReLU implementation."""

    def __init__(self, ):
        pass

    def forward(self, x):
        """Forward pass through ReLU."""
        return x

    def extra_repr(self, ):
        return f'ReLU({self.__dict__})'

