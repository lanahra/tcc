import json
import os
from os import path
from os.path import dirname, abspath, basename
from pprint import pprint

from second import solve


def edges_from(network):
    edges = {}
    for e in network['edges']:
        edges[e['id']] = (e['source'], e['target'])
    return edges


def verify(network, solution):
    edges = sorted([e['id'] for e in network['edges']])
    covered_edges = sorted([e for s in solution for e in s])

    return edges == covered_edges


root_dir = dirname(dirname(abspath(__file__)))
network_dir = os.path.join(root_dir, 'networks')
solution_dir = os.path.join(root_dir, 'solutions')
if not os.path.exists(solution_dir):
    os.makedirs(solution_dir)

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

network_path = path.join(root_dir, 'networks', 'zoo_394_30895.json')
print('Instance: {}'.format(basename(network_path)))

with open(network_path, 'r') as network_file:
    network = json.load(network_file)

    s = []
    valid = False

    flows = network['flows']
    edges = edges_from(network)
    s, l, e = solve(flows)
    valid = verify(network, s)

    # print('Leftovers: ' + str(l))
    # print(s)
    print(len(s))
    print(len(l))

    # pprint([list(map(lambda x: edges[x], e)) for e in flows])
    # sol = {k + 1: list(map(lambda x: edges[x], v)) for k, v in e.items()}
    # pprint(sol)
