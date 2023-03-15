#include "Engine.h"
#include <queue>

namespace neuralforge {

void AutogradEngine::execute(const std::vector<GradFn*>& roots) {
  std::queue<GradFn*> q;
  for (auto* r : roots) q.push(r);
  while (!q.empty()) {
    auto* fn = q.front(); q.pop();
    fn->apply();
  }
}

} // namespace neuralforge
