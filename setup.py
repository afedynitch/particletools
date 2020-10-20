# -*- coding: utf-8 -*-
import setuptools
from distutils.core import setup

__version__ = "1.1.6"


def setup_package():
    from os.path import abspath, dirname, join
    import sys

    this_directory = abspath(dirname(__file__))
    if sys.version_info.major == 3:
        with open(join(this_directory, 'README.md'), encoding='utf-8') as f:
            long_description = f.read()
    else:
        with open(join(this_directory, 'README.md')) as f:
            long_description = f.read()

    skip_marker = "# particletools"
    long_description = long_description[long_description.index(skip_marker) :].lstrip()

    arguments = dict(
        name='particletools',
        version=__version__,
        author='Anatoli Fedynitch',
        author_email='afedynitch@gmail.com',
        description='Translating particle codes from CR models from/to PDG codes',
        long_description=long_description,
        long_description_content_type='text/markdown',
        license="MIT",
        url='https://github.com/afedynitch/particletools',
        package_dir={'particletools': 'particletools'},
        packages=['particletools'],
        install_requires=['setuptools'],
        tests_require=['pytest'],
        py_modules=["six"],
        package_data={'particletools': ['ParticleData.xml']},
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Topic :: Scientific/Engineering :: Physics',
            'Intended Audience :: Science/Research',
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: MIT License'
        ],
    )

    setup(**arguments)

if __name__ == '__main__':
    setup_package()
