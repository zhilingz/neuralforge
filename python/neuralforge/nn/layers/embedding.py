"""Embedding layer implementation."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.nn.module import Module

__all__ = ['Embedding']


class Embedding(Module):
    """Embedding implementation."""

    def __init__(self, num_embeddings: int, embedding_dim: int):
        self.num_embeddings = num_embeddings
        self.embedding_dim = embedding_dim

    def forward(self, x):
        """Forward pass through Embedding."""
        return x

    def extra_repr(self, ):
        return f'Embedding({self.__dict__})'

