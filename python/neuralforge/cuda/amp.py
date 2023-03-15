"""Automatic mixed precision."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['autocast']


class autocast(object):
    """autocast implementation."""

    def __init__(self, dtype: str = 'float16'):
        self.dtype = dtype

    def __enter__(self, ):
        return self

    def __exit__(self, *args):
        pass

