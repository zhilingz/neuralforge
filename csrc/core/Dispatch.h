#pragma once
#include "TensorImpl.h"

namespace neuralforge {

template<typename Func>
void dispatch(DType dtype, Func&& func) {
  switch(dtype) {
    case DType::Float32: func.template operator()<float>(); break;
    case DType::Float64: func.template operator()<double>(); break;
    default: break;
  }
}

} // namespace neuralforge
