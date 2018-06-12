from __future__ import print_function
from particletools.tables import PYTHIAParticleData
import math

pdata = PYTHIAParticleData()

print("List all particles except intermediate species, sorted by life-time")

particles = []
for pid, pd in pdata.iteritems():
    if '~' not in pd.name:
        particles.append((pid, pd))

def cmp(a, b):
    ctau = lambda x: 0 if math.isnan(x[1].ctau) else x[1].ctau
    cta = ctau(a)
    ctb = ctau(b)
    if cta == ctb:
        return 0
    if cta < ctb:
        return -1
    return 1
particles.sort(cmp)

print('{:18s} {:>10} {:>10} {:>10} {:>6}'.format("name", "PDG ID", "mass[GeV]",
                                             "ctau[cm]", "charge"))

for pid, pd in particles:
    print('{name:18} {pid:10} {mass:10.3g} {ctau:10.3e} {charge:6.2g}'
          .format(name=pd.name, pid=pid, mass=pd.mass,
                  ctau=pd.ctau, charge=pd.charge))