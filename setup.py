#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='pyramidal',
    version='0.0.0',
    description='Neuroscience and Machine Learning Library at Neuronal Intelligence Lab',
    author='Fabian Sinz',
    author_email='fabian.sinz@uni-tuebingen.de',
    url='https://github.com/sinzlab/pyramidal',
    packages=find_packages(exclude=[]),
    install_requires=['numpy', 'tqdm', 'datajoint', 'attorch', 'pandas', 'h5py', 'pytorch'],
)
