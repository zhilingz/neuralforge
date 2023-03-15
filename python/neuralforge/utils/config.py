"""Configuration management."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['Config']


class Config(dict):
    """Config implementation."""

    def __init__(self, ):
        pass

    def from_file(self, path: str):
        return Config()

    def to_file(self, path: str):
        pass

