from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("integration",
              ["integration.pyx"],
              extra_compile_args=["-ffast-math"])]

setup(
  name="integration",
  cmdclass={"build_ext": build_ext},
  ext_modules=ext_modules)
