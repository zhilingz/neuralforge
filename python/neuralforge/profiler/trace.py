"""Execution tracing."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['Tracer']


class Tracer(object):
    """Tracer implementation."""

    def __init__(self, enabled: bool = True):
        self.enabled = enabled

    def start(self, ):
        pass

    def stop(self, ):
        pass

    def export_chrome_trace(self, path: str):
        pass

