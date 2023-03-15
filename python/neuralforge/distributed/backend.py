"""Distributed DistributedBackend."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['DistributedBackend']


class DistributedBackend(object):
    """DistributedBackend implementation."""

    def __init__(self, backend: str = 'nccl'):
        self.backend = backend

    def init_process_group(self, world_size: int, rank: int):
        """Initialize distributed."""
        self.world_size = world_size
        self.rank = rank

