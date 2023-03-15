#pragma once
#include <cstdlib>

namespace neuralforge {

class Allocator {
public:
  virtual ~Allocator() = default;
  virtual void* allocate(size_t size) = 0;
  virtual void deallocate(void* ptr) = 0;
};

class CPUAllocator : public Allocator {
public:
  void* allocate(size_t size) override;
  void deallocate(void* ptr) override;
};

} // namespace neuralforge
