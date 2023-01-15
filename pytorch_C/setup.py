from setuptools import setup, Extension
import pybind11
import torch
from torch.utils import cpp_extension

cpp_args = ['-std=c++11', '-stdlib=libc++', '-mmacosx-version-min=10.7']

sfc_module = Extension(
    'pytorch_C',
    sources=['Source.cpp'],
    include_dirs=[pybind11.get_include()],
    language='c++',
    extra_compile_args=cpp_args,
    )
torch_H=Extension(
   name='Source.cpp',
   sources=['Source.cpp'],
   include_dirs=cpp_extension.include_paths(),
   language='c++')

setup(
    name='pytorch_C',
    version='1.0',
    description='Python package with superfastcode2 C++ extension (PyBind11)',
    ext_modules=[torch_H,sfc_module],
    cmdclass={'build_ext': cpp_extension.BuildExtension}
)