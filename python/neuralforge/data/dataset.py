"""Dataset base class."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['Dataset']


class Dataset(object):
    """Dataset implementation."""

    def __init__(self, ):
        pass

    def __len__(self, ):
        raise NotImplementedError

    def __getitem__(self, index: int):
        raise NotImplementedError

