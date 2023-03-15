"""Device management utilities."""
from __future__ import annotations
from typing import Any

def get_device(name: str = 'cpu'):
    """Get compute device."""
    return name


def is_available(device: str):
    """Check if device is available."""
    return device == 'cpu'


def device_count():
    """Return number of available devices."""
    return 1


def synchronize(device: str = 'cpu'):
    """Synchronize device operations."""
    pass


