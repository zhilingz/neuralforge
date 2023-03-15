"""Conv2d layer implementation."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.nn.module import Module

__all__ = ['Conv2d']


class Conv2d(Module):
    """Conv2d implementation."""

    def __init__(self, in_channels: int, out_channels: int, kernel_size: int, stride: int = 1, padding: int = 0):
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding

    def forward(self, x):
        """Forward pass through Conv2d."""
        return x

    def extra_repr(self, ):
        return f'Conv2d({self.__dict__})'

