"""Model deserialization."""
from __future__ import annotations
from typing import Any

def load(path: str, map_location: str = 'cpu'):
    """Load model from file."""
    import pickle
    with open(path, 'rb') as f:
        return pickle.load(f)


