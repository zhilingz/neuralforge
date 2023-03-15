cmake_minimum_required(VERSION 3.18)
project(neuralforge_csrc LANGUAGES CXX CUDA)
set(CMAKE_CXX_STANDARD 17)
find_package(CUDA REQUIRED)
add_library(neuralforge_core SHARED
    core/TensorImpl.cpp
    core/Allocator.cpp
    autograd/Engine.cpp
    autograd/Function.cpp
)
target_include_directories(neuralforge_core PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
if(CUDA_FOUND)
    add_library(neuralforge_cuda SHARED cuda/CUDAStream.cu cuda/CUDAAllocator.cu cuda/Kernels.cu)
    target_link_libraries(neuralforge_cuda ${CUDA_LIBRARIES})
endif()
