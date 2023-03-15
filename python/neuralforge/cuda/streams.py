"""CUDA stream management."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['CUDAStream']


class CUDAStream(object):
    """CUDAStream implementation."""

    def __init__(self, device_index: int = 0):
        self.device_index = device_index

    def synchronize(self, ):
        pass

    def wait_stream(self, stream):
        pass

