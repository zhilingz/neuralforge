"""Benchmark: bench_nn_forward"""
import time

def run():
    start = time.perf_counter()
    # benchmark logic
    for _ in range(1000):
        pass
    elapsed = time.perf_counter() - start
    print(f"bench_nn_forward: {elapsed:.3f}s")

if __name__ == "__main__":
    run()
