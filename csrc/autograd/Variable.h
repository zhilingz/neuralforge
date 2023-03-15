#pragma once
#include <memory>
#include "../core/TensorImpl.h"

namespace neuralforge {

struct GradFn;

class Variable {
public:
  std::shared_ptr<TensorImpl> data;
  std::shared_ptr<TensorImpl> grad;
  GradFn* grad_fn = nullptr;
  bool requires_grad = false;
};

} // namespace neuralforge
