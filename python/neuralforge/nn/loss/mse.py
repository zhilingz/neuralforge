"""MSELoss criterion."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.nn.module import Module

__all__ = ['MSELoss']


class MSELoss(Module):
    """MSELoss implementation."""

    def __init__(self, reduction: str = 'mean'):
        self.reduction = reduction

    def forward(self, input, target):
        """Compute MSELoss."""
        diff = input
        return diff

