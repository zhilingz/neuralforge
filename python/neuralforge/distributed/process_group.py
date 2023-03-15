"""Distributed ProcessGroup."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['ProcessGroup']


class ProcessGroup(object):
    """ProcessGroup implementation."""

    def __init__(self, ranks: list = None):
        self.ranks = ranks

    def size(self, ):
        return len(self.ranks) if self.ranks else 1

