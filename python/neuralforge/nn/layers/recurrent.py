"""LSTM layer implementation."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.nn.module import Module

__all__ = ['LSTM']


class LSTM(Module):
    """LSTM implementation."""

    def __init__(self, input_size: int, hidden_size: int, num_layers: int = 1, bidirectional: bool = False):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.bidirectional = bidirectional

    def forward(self, x):
        """Forward pass through LSTM."""
        return x

    def extra_repr(self, ):
        return f'LSTM({self.__dict__})'

