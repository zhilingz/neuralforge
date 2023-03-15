# NeuralForge

A deep learning framework for research and production.

![CI](https://github.com/neuralforge/neuralforge/workflows/CI/badge.svg)
![PyPI](https://img.shields.io/pypi/v/neuralforge)
![npm](https://img.shields.io/npm/v/@neuralforge/core)

## Installation

```bash
pip install neuralforge
```

```bash
npm install @neuralforge/core
```

## Quick Start

```python
import neuralforge as nf
from neuralforge.nn import Linear, Module
from neuralforge.optim import Adam

class MLP(Module):
    def __init__(self):
        super().__init__()
        self.fc1 = Linear(784, 256)
        self.fc2 = Linear(256, 10)

    def forward(self, x):
        x = nf.nn.functional.relu(self.fc1(x))
        return self.fc2(x)

model = MLP()
optimizer = Adam(model.parameters(), lr=0.001)
```

## Features

- Automatic differentiation
- GPU acceleration (CUDA)
- Distributed training (DDP, FSDP)
- Model hub for pretrained models
- JavaScript inference SDK
- Training visualization dashboard

## Documentation

See [docs/](./docs/) for full documentation.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).
