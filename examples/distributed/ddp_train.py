"""Distributed Data Parallel training example."""
import neuralforge as nf
from neuralforge.distributed import DistributedBackend

def main():
    backend = DistributedBackend(backend='nccl')
    backend.init_process_group(world_size=4, rank=0)
    print(f"Rank 0 initialized")
    # Training loop would go here

if __name__ == "__main__":
    main()
