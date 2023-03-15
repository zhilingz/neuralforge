"""Model hub cache operations."""
from __future__ import annotations
from typing import Any

def get_cache_dir():
    """Get cache directory."""
    import os
    return os.path.expanduser('~/.cache/neuralforge')


def clear_cache():
    """Clear model cache."""
    pass


