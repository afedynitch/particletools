from particletools.tables import PYTHIAParticleData, print_decay_channels
import argparse
import six

pyth_data = PYTHIAParticleData()

parser = argparse.ArgumentParser()
parser.add_argument("pid_or_name", default="Ds+")
args = parser.parse_args()

try:
    pid = int(args.pid_or_name)
except ValueError:
    pid = pyth_data.pdg_id(args.pid_or_name)

pd = pyth_data[pid]

print('List decay channels and branching ratios of {} (ID={})'.format(pd.name, pid))
print_decay_channels(pid, pyth_data)
