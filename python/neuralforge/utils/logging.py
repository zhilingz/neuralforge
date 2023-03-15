"""Logging utilities."""
from __future__ import annotations
from typing import Any

def get_logger(name: str):
    """Get named logger."""
    import logging
    return logging.getLogger(name)


def setup_logging(level: str = 'INFO'):
    """Setup logging config."""
    import logging
    logging.basicConfig(level=level)


