#include "TensorImpl.h"

namespace neuralforge {

TensorImpl::TensorImpl(const std::vector<int64_t>& shape, DType dtype)
    : shape_(shape), dtype_(dtype), data_(nullptr) {
  numel_ = 1;
  for (auto s : shape_) numel_ *= s;
  data_ = std::malloc(numel_ * dtype_size(dtype_));
}

TensorImpl::~TensorImpl() { std::free(data_); }

} // namespace neuralforge
