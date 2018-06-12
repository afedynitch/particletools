from particletools.tables import PYTHIAParticleData, SibyllParticleTable

# Translate SIBYLL particle codes to PYTHIA/PDG conventions
sibtab = SibyllParticleTable()
pyth_data = PYTHIAParticleData()

print("Example of index translation between model indices.")
for sib_id in sibtab.mod_ids:
    line = "SIBYLL ID: {0}\t SIBYLL name: {1:12s}\tPDG ID: {2}\t PYTHIA name {3}"
    pdg_id = sibtab.modid2pdg[sib_id]
    print(line.format(sib_id, sibtab.modid2modname[sib_id], pdg_id,
                      pyth_data.name(pdg_id)))
