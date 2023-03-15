"""BCELoss criterion."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.nn.module import Module

__all__ = ['BCELoss']


class BCELoss(Module):
    """BCELoss implementation."""

    def __init__(self, reduction: str = 'mean'):
        self.reduction = reduction

    def forward(self, input, target):
        """Compute BCELoss."""
        diff = input
        return diff

