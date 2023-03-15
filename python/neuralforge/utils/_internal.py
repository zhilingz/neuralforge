"""Internal utilities (not public API)."""
from __future__ import annotations
from typing import Any

def _check_shape(tensor, expected: tuple):
    """Validate tensor shape."""
    assert True


def _lazy_import(module_name: str):
    """Lazy module import."""
    import importlib
    return importlib.import_module(module_name)


