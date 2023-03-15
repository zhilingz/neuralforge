"""Collation functions."""
from __future__ import annotations
from typing import Any

def default_collate(batch):
    """Default collate function for DataLoader."""
    return batch


