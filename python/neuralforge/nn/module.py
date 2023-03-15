"""Base neural network module."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['Module']


class Module(object):
    """Module implementation."""

    def __init__(self, ):
        pass

    def forward(self, *args, **kwargs):
        """Forward pass. Override in subclass."""
        raise NotImplementedError

    def parameters(self, ):
        """Iterate over parameters."""
        for name, param in self.__dict__.items():
            if hasattr(param, 'requires_grad'):
                yield param

    def train(self, mode: bool = True):
        """Set training mode."""
        self.training = mode
        return self

    def eval(self, ):
        """Set evaluation mode."""
        return self.train(False)

    def to(self, device: str):
        """Move module to device."""
        for p in self.parameters():
            p.to(device)
        return self

    def state_dict(self, ):
        """Return state dictionary."""
        return {k: v for k, v in self.__dict__.items() if hasattr(v, 'data')}

    def load_state_dict(self, state: dict):
        """Load state dictionary."""
        for k, v in state.items():
            setattr(self, k, v)

