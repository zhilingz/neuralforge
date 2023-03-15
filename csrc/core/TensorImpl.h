#pragma once
#include <vector>
#include <cstdint>
#include <cstdlib>

namespace neuralforge {

enum class DType { Float32, Float64, Float16, Int32, Int64 };

inline size_t dtype_size(DType d) {
  switch(d) { case DType::Float32: return 4; case DType::Float64: return 8; default: return 4; }
}

class TensorImpl {
public:
  TensorImpl(const std::vector<int64_t>& shape, DType dtype);
  ~TensorImpl();
  const std::vector<int64_t>& shape() const { return shape_; }
  int64_t numel() const { return numel_; }
  void* data() { return data_; }
private:
  std::vector<int64_t> shape_;
  DType dtype_;
  int64_t numel_;
  void* data_;
};

} // namespace neuralforge
