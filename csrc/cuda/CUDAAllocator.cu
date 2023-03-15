#include <cuda_runtime.h>
#include "../core/Allocator.h"

namespace neuralforge {

class CUDAAllocator : public Allocator {
public:
  void* allocate(size_t size) override {
    void* ptr; cudaMalloc(&ptr, size); return ptr;
  }
  void deallocate(void* ptr) override { cudaFree(ptr); }
};

} // namespace neuralforge
