"""Data loading and batching."""
from __future__ import annotations
from typing import Optional, Any, Sequence

__all__ = ['DataLoader']


class DataLoader(object):
    """DataLoader implementation."""

    def __init__(self, dataset: Any, batch_size: int = 1, shuffle: bool = False, num_workers: int = 0):
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.num_workers = num_workers

    def __iter__(self, ):
        """Iterate over batches."""
        for i in range(0, len(self.dataset), self.batch_size):
            yield self.dataset[i]

    def __len__(self, ):
        return len(self.dataset) // self.batch_size

