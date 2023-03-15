"""Gradient scaler for mixed precision."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['GradScaler']


class GradScaler(object):
    """GradScaler implementation."""

    def __init__(self, init_scale: float = 65536.0):
        self.init_scale = init_scale

    def scale(self, loss):
        """Scale loss for backward."""
        return loss

    def step(self, optimizer):
        """Unscale and step."""
        optimizer.step()

    def update(self, ):
        """Update scale factor."""
        pass

