import os
import re
import json
from pprint import pprint
from os.path import dirname, abspath
from os import path

root_dir = dirname(dirname(abspath(__file__)))


def make_network(data):
    network = {}
    network['nodes'] = []
    network['edges'] = []
    network['flows'] = []
    network['capacity'] = 5

    p = re.compile('set V :=((?: \d+)+);$', re.M)
    m = p.search(data)
    network['nodes'] = m.groups()[0].strip().split()

    p = re.compile('set A :=([ \d\n]*);')
    m = p.search(data)
    edges = m.groups()[0].strip().split()

    id = 0
    for i in range(0, len(edges), 2):
        edge = {'id': id, 'source': edges[i], 'target': edges[i + 1]}
        id = id + 1
        network['edges'].append(edge)

    p = re.compile('set F\[\d+\] :=([ \d\n]*);')
    matcher = re.finditer(p, data)
    for m in matcher:
        edges = m.groups()[0].strip().split()
        flow = []

        for i in range(0, len(edges), 2):
            edge = (edges[i], edges[i + 1])
            flow.append(get_id(edge, network['edges']))

        network['flows'].append(flow)

    return network


def get_id(edge, edges):
    for e in edges:
        if e['source'] == edge[0] and e['target'] == edge[1]:
            return e['id']


def main():
    topologies_dir = path.join(root_dir, 'topologies')
    topologies_paths = [
        path.join(topologies_dir, t, 'input.dat')
        for t in os.listdir(topologies_dir)
    ]

    network_dir = path.join(root_dir, 'network')
    if not path.exists(network_dir):
        os.makedirs(network_dir)

    for topology_path in topologies_paths:
        topology_name = path.basename(
            abspath(path.join(topology_path, os.pardir)))
        print(topology_name)

        with open(topology_path) as topology_file:
            data = topology_file.read()

        network = make_network(data)

        with open(
                path.join(network_dir, '{}.json'.format(topology_name)),
                'w') as f:
            json.dump(network, f, indent=2)


if __name__ == '__main__':
    main()
