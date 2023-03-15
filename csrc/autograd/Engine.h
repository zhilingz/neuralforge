#pragma once
#include <vector>
#include "Variable.h"

namespace neuralforge {

struct GradFn {
  virtual ~GradFn() = default;
  virtual void apply() = 0;
  std::vector<GradFn*> next_functions;
};

class AutogradEngine {
public:
  static AutogradEngine& get_instance() { static AutogradEngine e; return e; }
  void execute(const std::vector<GradFn*>& roots);
};

} // namespace neuralforge
