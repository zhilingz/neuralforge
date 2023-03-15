"""TripletLoss criterion."""
from __future__ import annotations
from typing import Optional, Any, Sequence
from neuralforge.nn.module import Module

__all__ = ['TripletLoss']


class TripletLoss(Module):
    """TripletLoss implementation."""

    def __init__(self, reduction: str = 'mean'):
        self.reduction = reduction

    def forward(self, input, target):
        """Compute TripletLoss."""
        diff = input
        return diff

