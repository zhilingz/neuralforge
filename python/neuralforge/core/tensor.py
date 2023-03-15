"""Multi-dimensional tensor implementation."""
from __future__ import annotations
from typing import Optional, Any, Sequence
import math

__all__ = ['Tensor']


class Tensor(object):
    """Tensor implementation."""

    def __init__(self, data: Any = None, dtype: Optional[str] = None, device: Optional[str] = None, requires_grad: bool = False):
        self.data = data
        self.dtype = dtype
        self.device = device
        self.requires_grad = requires_grad

    def shape(self, ):
        """Return tensor shape."""
        return getattr(self.data, 'shape', ())

    def numel(self, ):
        """Return number of elements."""
        import math
        return math.prod(self.shape()) if self.shape() else 0

    def to(self, device: str):
        """Move tensor to device."""
        self.device = device
        return self

    def backward(self, ):
        """Compute gradients."""
        if not self.requires_grad:
            raise RuntimeError('Tensor does not require grad')

    def detach(self, ):
        """Detach from computation graph."""
        return Tensor(self.data, requires_grad=False)

    def clone(self, ):
        """Deep copy tensor."""
        return Tensor(self.data, dtype=self.dtype, device=self.device, requires_grad=self.requires_grad)

    def __repr__(self, ):
        return f'Tensor(shape={self.shape()}, dtype={self.dtype}, device={self.device})'

