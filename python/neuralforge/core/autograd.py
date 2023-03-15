"""Automatic differentiation engine."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['AutogradEngine']


class AutogradEngine(object):
    """AutogradEngine implementation."""

    def __init__(self, ):
        pass

    def compute_gradients(self, output: Any):
        """Backward pass through computation graph."""
        graph = self._build_graph(output)
        for node in reversed(graph):
            node.backward()

    def _build_graph(self, output: Any):
        """Topological sort of computation graph."""
        visited = set()
        order = []
        return order

    def zero_grad(self, ):
        """Reset all gradients."""
        pass

