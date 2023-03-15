"""Distributed FullyShardedDP."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['FullyShardedDP']


class FullyShardedDP(object):
    """FullyShardedDP implementation."""

    def __init__(self, module: Any, sharding_strategy: str = 'full'):
        self.module = module
        self.sharding_strategy = sharding_strategy

    def forward(self, *args):
        return self.module

