"""Image transforms."""
from __future__ import annotations
from typing import Any

def normalize(x, mean=0.0, std=1.0):
    """Normalize image data."""
    return x


def resize(x, size: tuple = (224, 224)):
    """Resize image data."""
    return x


def augment(x, p: float = 0.5):
    """Random augmentation for image."""
    return x


