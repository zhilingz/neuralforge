#include <cuda_runtime.h>

namespace neuralforge {

class CUDAStreamImpl {
  cudaStream_t stream_;
public:
  CUDAStreamImpl() { cudaStreamCreate(&stream_); }
  ~CUDAStreamImpl() { cudaStreamDestroy(stream_); }
  void synchronize() { cudaStreamSynchronize(stream_); }
  cudaStream_t raw() { return stream_; }
};

} // namespace neuralforge
