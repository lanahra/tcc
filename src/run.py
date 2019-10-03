import json
import os
from os import path
from os.path import dirname, abspath, basename
from pprint import pprint

from heuristic import solve


def edges_from(network):
    edges = {}
    for e in network['edges']:
        edges[e['id']] = (e['source'], e['target'])
    return edges


def is_valid(network, k, solution):
    edges = sorted([e['id'] for e in network['edges']])
    covered_edges = sorted([e for s in solution for e in s])

    return edges == covered_edges and all(len(s) <= k for s in solution)


root_dir = dirname(dirname(abspath(__file__)))
network_dir = os.path.join(root_dir, 'networks')

# network_paths = sorted(
#     [os.path.join(network_dir, f) for f in os.listdir(network_dir)])
# for network_path in network_paths:
#     print('Job: {}'.format(network_path))
#     with open(network_path, 'r') as network_file:
#         network = json.load(network_file)
#         flows = network['flows']
#         s, l = solve(flows)

#         if not l:
#             print(len(s))

network_paths = sorted(
    [os.path.join(network_dir, f) for f in os.listdir(network_dir)])
for network_path in network_paths:
    # network_path = path.join(root_dir, 'networks', 'zoo_394_38612.json')
    print('Instance: {}'.format(basename(network_path)))

    with open(network_path, 'r') as network_file:
        network = json.load(network_file)
        interfaces = [e['id'] for e in network['edges']]
        # flows = list(enumerate(network['flows']))
        flows = network['flows']
        k = 5

        s = solve(interfaces, flows, k)
        if not is_valid(network, k, s):
            raise Exception

    # break
