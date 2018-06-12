from __future__ import print_function
from particletools.tables import (PYTHIAParticleData, c_speed_of_light,
                                  print_stable, make_stable_list)
import math

pdata = PYTHIAParticleData()

print_stable(pdata.ctau('D0') / c_speed_of_light,
             title=('Particles with known finite lifetimes longer '
                    'than that of D0 ({0}cm)').format(pdata.ctau('D0')))
print()
print('Known particles with tau > 1e-8s:', make_stable_list(1e-8))
