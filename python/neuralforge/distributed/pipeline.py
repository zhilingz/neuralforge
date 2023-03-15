"""Distributed PipelineParallel."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['PipelineParallel']


class PipelineParallel(object):
    """PipelineParallel implementation."""

    def __init__(self, num_stages: int = 2):
        self.num_stages = num_stages

    def forward(self, x):
        return x

