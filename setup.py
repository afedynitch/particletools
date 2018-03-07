# -*- coding: utf-8 -*-
from setuptools import setup

__version__ = "0.1"

long_description = ''.join(open('README.rst').readlines()[4:])

setup(
    name='particletools',
    version=__version__,
    author='Anatoli Fedynitch',
    author_email='afedynitch@gmail.com',
    description='Translating particle codes from CR models from/to PDG codes',
    long_description=long_description,
    license="MIT",
    url='https://gitlab.com/afedynitch/ParticleDataTool',
    package_dir={'particletools': 'particletools'},
    packages=['particletools'],
    install_requires=['setuptools'],
    data_files=[('particletools', ['particletools/ParticleData.xml'])],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Physics',
        'Intended Audience :: Science/Research',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License'
    ],
)
