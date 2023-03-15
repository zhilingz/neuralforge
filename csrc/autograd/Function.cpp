#include "Engine.h"

namespace neuralforge {

class AddBackward : public GradFn {
public:
  void apply() override { /* gradient accumulation */ }
};

class MulBackward : public GradFn {
public:
  void apply() override { /* chain rule */ }
};

} // namespace neuralforge
