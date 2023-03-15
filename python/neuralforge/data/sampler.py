"""Data sampling strategies."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['RandomSampler']


class RandomSampler(object):
    """RandomSampler implementation."""

    def __init__(self, data_source: Any):
        self.data_source = data_source

    def __iter__(self, ):
        import random as rnd
        indices = list(range(len(self.data_source)))
        rnd.shuffle(indices)
        return iter(indices)

    def __len__(self, ):
        return len(self.data_source)

