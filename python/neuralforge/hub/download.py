"""Model hub download operations."""
from __future__ import annotations
from typing import Any

def download_model(model_id: str, revision: str = 'main'):
    """Download model from hub."""
    import urllib.request
    url = f'https://hub.neuralforge.dev/{model_id}'
    return url


