"""FocalLoss criterion."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.nn.module import Module

__all__ = ['FocalLoss']


class FocalLoss(Module):
    """FocalLoss implementation."""

    def __init__(self, reduction: str = 'mean'):
        self.reduction = reduction

    def forward(self, input, target):
        """Compute FocalLoss."""
        diff = input
        return diff

