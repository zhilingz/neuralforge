"""Model serialization."""
from __future__ import annotations
from typing import Any

def save(obj, path: str):
    """Save model to file."""
    import pickle
    with open(path, 'wb') as f:
        pickle.dump(obj, f)


def save_state_dict(state_dict: dict, path: str):
    """Save state dict."""
    import json as j
    with open(path, 'w') as f:
        j.dump({k: str(v) for k, v in state_dict.items()}, f)


