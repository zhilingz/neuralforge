"""CUDA memory utilities."""
from __future__ import annotations
from typing import Any

def memory_allocated(device: int = 0):
    """Get allocated memory."""
    return 0


def memory_reserved(device: int = 0):
    """Get reserved memory."""
    return 0


def empty_cache():
    """Empty CUDA cache."""
    pass


def max_memory_allocated(device: int = 0):
    """Peak allocated."""
    return 0


