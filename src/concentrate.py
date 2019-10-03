import json
import os
from os import path
from os.path import dirname, abspath, basename
from pprint import pprint
from copy import deepcopy
from random import sample


def flows_through(interface, flows):
    return [f[0] for f in flows if interface in f[1]]


def concentrate(interfaces, flows, k):
    covered_by = {i: None for i in interfaces}
    monitors = {f[0]: [] for f in flows}
    capacity = {f[0]: min(len(f[1]), k) for f in flows}
    nif = {f[0]: len(f[1]) for f in flows}
    sif = {
        f[0]: sorted(f[1], key=lambda i: len(flows_through(i, flows)))
        for f in flows
    }
    uf = deepcopy(flows)

    while uf and any(not covered_by[i] for i in interfaces):
        f_max = max(uf, key=lambda f: (nif[f[0]], capacity[f[0]]))[0]
        uf = [f for f in uf if f[0] != f_max]

        for i in sif[f_max]:
            if not covered_by[i] and capacity[f_max] >= 1:
                covered_by[i] = f_max
                monitors[f_max].append(i)
                capacity[f_max] -= 1
                for f in flows_through(i, flows):
                    nif[f] -= 1


root_dir = dirname(dirname(abspath(__file__)))
network_path = path.join(root_dir, 'networks', 'zoo_14_17.json')
print('Instance: {}'.format(basename(network_path)))

with open(network_path, 'r') as network_file:
    network = json.load(network_file)
    interfaces = [e['id'] for e in network['edges']]
    flows = list(enumerate(network['flows']))

    concentrate(interfaces, flows, 5)
