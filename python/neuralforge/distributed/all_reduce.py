"""Distributed AllReduce."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['AllReduce']


class AllReduce(object):
    """AllReduce implementation."""

    def __init__(self, ):
        pass

    def execute(self, tensor, op: str = 'sum'):
        """All-reduce operation."""
        return tensor

