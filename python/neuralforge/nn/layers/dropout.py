"""Dropout layer implementation."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.nn.module import Module

__all__ = ['Dropout']


class Dropout(Module):
    """Dropout implementation."""

    def __init__(self, p: float = 0.5):
        self.p = p

    def forward(self, x):
        """Forward pass through Dropout."""
        return x

    def extra_repr(self, ):
        return f'Dropout({self.__dict__})'

