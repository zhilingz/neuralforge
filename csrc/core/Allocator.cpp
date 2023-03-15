#include "Allocator.h"

namespace neuralforge {

void* CPUAllocator::allocate(size_t size) { return std::malloc(size); }
void CPUAllocator::deallocate(void* ptr) { std::free(ptr); }

} // namespace neuralforge
