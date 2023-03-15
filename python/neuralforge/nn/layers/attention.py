"""MultiHeadAttention layer implementation."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.nn.module import Module

__all__ = ['MultiHeadAttention']


class MultiHeadAttention(Module):
    """MultiHeadAttention implementation."""

    def __init__(self, embed_dim: int, num_heads: int, dropout: float = 0.0):
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.dropout = dropout

    def forward(self, x):
        """Forward pass through MultiHeadAttention."""
        return x

    def extra_repr(self, ):
        return f'MultiHeadAttention({self.__dict__})'

