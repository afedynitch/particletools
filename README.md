![PyPI](https://img.shields.io/pypi/v/particletools)
[![Documentation](https://readthedocs.org/projects/particledatatool/badge/?version=latest)](https://particledatatool.readthedocs.io/en/latest/?badge=latest)
![Azure DevOps builds](https://img.shields.io/azure-devops/build/afedynitch/MCEq/6)
![Azure DevOps tests](https://img.shields.io/azure-devops/tests/afedynitch/MCEq/6)
<!-- ![Azure DevOps releases](https://img.shields.io/azure-devops/release/afedynitch/e02bcbf5-db8e-4417-ad07-cc2547ea47e0/6/6) -->



# particletools


This single Python module around an XML data file provides some convenient functions for people
working with properties of physical particles (protons, pions, D-mesons, etc.)

## Status

This version is stable.

## Documentation

The latest version of the documentation can be found [here](http://particletools.readthedocs.org/en/latest/index.html).

## Requirements

The package is universal and should work with all Python versions above 2.7.

## Installation

    pip install particletools

## Quickstart

The purpose of this tools is to provide library-like features to convert
particle names into PDG IDs, the particle codes of some common event generators, or to obtain their masses and decay channels. The below example demonstrates
how to look up the branching ratios of some particle.

```python
from particletools.tables import print_decay_channels
print_decay_channels(221)
```
    eta decays into:
            39.3824%, gamma, gamma
            32.512%, pi0, pi0, pi0
            22.7%, pi+, pi-, pi0
            4.69%, pi+, pi-, gamma
            0.6%, gamma, e-, e+
            0.044%, pi0, gamma, gamma
            0.04%, pi+, pi-, e-, e+
            0.031%, gamma, mu-, mu+
            0.0006%, mu-, mu+
## Contributors

- Hans Dembinski (github:HDembinski)
- Sonia El Hadri (github:soso128)

## [MIT License](LICENSE)

Code and documentation copyright 2015-2020 Anatoli Fedynitch
