"""NeuralForge — A deep learning framework for research and production."""
__version__ = "0.9.0"
from neuralforge.core.tensor import Tensor
from neuralforge.core.device import get_device, is_available
from neuralforge.nn.module import Module
from neuralforge.nn.parameter import Parameter
