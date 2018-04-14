.. particletools documentation master file, created by
   sphinx-quickstart on Fri Nov 28 12:04:38 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

:py:mod:`particletools` documentation 
=====================================

.. toctree::
   :maxdepth: 2

````````````
Introduction
````````````
The module :mod:`particletools.tables` is a convenience library for translating
particle codes from one particle event-generator into the more general
naming convention of the Particle Data Group `PDG <http://pdg.lbl.gov>`_.
It also gives you access to different properties of known particles,
such as their mass, charge, life-time and the known decay channels including
the branching ratio. 


The database :py:mod:`particletools` relies on an XML database that is part
of the `PYTHIA 8 <http://home.thep.lu.se/~torbjorn/pythia81html/Welcome.html>`_ 
Monte Carlo event-generator (GPLv2). Its popularity in the high-energy physics
community and continuous maintenance, I hope that this particle database is
well maintained. Of course, neither I, nor the PYTHIA developers, exclude
mistakes, outdated data, etc. It is up to your own responsibility as a researcher
to convince yourself that this piece of code produces output that fulfills your
quality requirements. Feel very encouraged to read 
`the 'comments on the data' <http://home.thep.lu.se/~torbjorn/pythia81html/ParticleData.html>`_
by the authors of this XML file.


The largest part of the information contained in this XML is ignored 
and could be subject for future extensions if needed. This version here
is based on the 2006 version of the PDG + things from 'PYTHIA'.


```````
Caching
```````
The instance of :class:`table.PYTHIAParticleData` parses the XML database
and saves pickles the content to a cache file in your working directory.
Subsequent instatiations of this class will try to load this file instead
of parsing the XML repeatedly. To force parsing the XML file again just
delete the file "ParticleData.ppl".


````````````````````
Module documentation
````````````````````

.. automodule:: tables
   :members:



Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

