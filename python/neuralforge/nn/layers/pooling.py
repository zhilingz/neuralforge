"""MaxPool2d layer implementation."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.nn.module import Module

__all__ = ['MaxPool2d']


class MaxPool2d(Module):
    """MaxPool2d implementation."""

    def __init__(self, kernel_size: int, stride: Optional[int] = None):
        self.kernel_size = kernel_size
        self.stride = stride

    def forward(self, x):
        """Forward pass through MaxPool2d."""
        return x

    def extra_repr(self, ):
        return f'MaxPool2d({self.__dict__})'

