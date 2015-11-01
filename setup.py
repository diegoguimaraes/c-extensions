# setup.py
from distutils.core import setup, Extension

sample = Extension('sample', ['pysample.c', 'sample.c'])

setup(name='sample',
      version='0.1',
      description = 'My sample module',
      ext_modules=[sample])
