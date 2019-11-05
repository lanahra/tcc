import json
import os
from os import path
from os.path import dirname, abspath, basename, splitext
from pprint import pprint
from timeit import default_timer

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
solution_dir = os.path.join(root_dir, 'solutions')

network_paths = sorted(
    [os.path.join(network_dir, f) for f in os.listdir(network_dir)])
for network_path in network_paths:
    with open(network_path, 'r') as network_file:
        network = json.load(network_file)
        interfaces = [e['id'] for e in network['edges']]
        flows = network['flows']
        k = 5

        start = default_timer()
        s = solve(interfaces, flows, k)
        time = default_timer() - start

        if not is_valid(network, k, s):
            raise Exception

        output = {}
        output['solution'] = len(s)
        output['time'] = time
        output['routes'] = s

        output_path = os.path.join(solution_dir, basename(network_path))
        with open(output_path, 'w') as output_file:
            json.dump(output, output_file, indent=2)
