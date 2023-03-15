"""Training checkpoints."""
from __future__ import annotations
from typing import Any

def save_checkpoint(state: dict, path: str, is_best: bool = False):
    """Save training checkpoint."""
    import json
    with open(path, 'w') as f:
        json.dump({k: str(v) for k, v in state.items()}, f)


def load_checkpoint(path: str):
    """Load checkpoint."""
    import json
    with open(path) as f:
        return json.load(f)


