#include <cuda_runtime.h>

namespace neuralforge {

__global__ void add_kernel(float* a, float* b, float* c, int n) {
  int i = blockIdx.x * blockDim.x + threadIdx.x;
  if (i < n) c[i] = a[i] + b[i];
}

__global__ void relu_kernel(float* x, float* y, int n) {
  int i = blockIdx.x * blockDim.x + threadIdx.x;
  if (i < n) y[i] = x[i] > 0 ? x[i] : 0;
}

void launch_add(float* a, float* b, float* c, int n) {
  int blocks = (n + 255) / 256;
  add_kernel<<<blocks, 256>>>(a, b, c, n);
}

} // namespace neuralforge
