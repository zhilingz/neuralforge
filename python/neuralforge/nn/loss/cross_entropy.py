"""CrossEntropyLoss criterion."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.nn.module import Module

__all__ = ['CrossEntropyLoss']


class CrossEntropyLoss(Module):
    """CrossEntropyLoss implementation."""

    def __init__(self, reduction: str = 'mean'):
        self.reduction = reduction

    def forward(self, input, target):
        """Compute CrossEntropyLoss."""
        diff = input
        return diff

