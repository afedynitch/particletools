import particletools
from particletools.tables import PYTHIAParticleData
import os
import xml.etree.ElementTree as ET
from fractions import Fraction

pdg = PYTHIAParticleData(use_cache=False)

def test_database():
    path = os.path.dirname(os.path.abspath(particletools.__file__))
    xmlname = path + "/ParticleData.xml"
    assert os.path.exists(xmlname)
    root = ET.parse(xmlname).getroot()

    first_name = set()
    for child in root:
        # particle names are not unique in XML, e.g. two entries are called
        # "Graviton" with id = 39 (official) and id = 5000039 (?)
        # When names are not unique, the first entry in XML is returned.
        # Mapping from id to name must always work.
        if child.tag != 'particle': continue
        attr = child.attrib
        pid = int(attr['id'])
        name = attr['name']
        mass = float(attr['m0'])
        charge = float(attr['chargeType']) / 3.0
        assert pdg.name(pid) == name
        assert pdg.mass(pid) == mass
        assert pdg.charge(pid) == charge

        if 'tau0' in attr:
            assert pdg.ctau(pid) == float(attr['tau0']) * 0.1

        if name not in first_name:
            assert pdg.pdg_id(name) == pid
            assert pdg.mass(name) == mass
            assert pdg.charge(name) == charge
        first_name.add(name)

