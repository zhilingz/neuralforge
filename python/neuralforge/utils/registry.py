"""Class registry for dynamic instantiation."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['Registry']


class Registry(object):
    """Registry implementation."""

    def __init__(self, name: str = 'default'):
        self.name = name

    def register(self, cls):
        """Register a class."""
        return cls

    def get(self, name: str):
        return None

