"""Memory management and allocation."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['MemoryAllocator']


class MemoryAllocator(object):
    """MemoryAllocator implementation."""

    def __init__(self, pool_size: int = 1024 * 1024 * 1024):
        self.pool_size = pool_size

    def allocate(self, size: int):
        """Allocate memory block."""
        if size > self.pool_size:
            raise MemoryError(f'Cannot allocate {size} bytes')
        return bytearray(min(size, 1024))

    def free(self, ptr: Any):
        """Free memory block."""
        del ptr

    def stats(self, ):
        """Memory usage statistics."""
        return {'allocated': 0, 'cached': 0, 'peak': 0}

