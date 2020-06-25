from pprint import pprint
from pulp import *
from os.path import dirname, abspath, basename
from timeit import default_timer
import os
import json

root_dir = dirname(dirname(abspath(__file__)))
network_dir = os.path.join(root_dir, 'networks')


def subtrails_of(trail, k=5):
    for i in range(1, min(k + 1, len(trail) + 1)):
        for s in map(list, zip(*[trail[j:] for j in range(i)])):
            yield s


def all_subtrails_of(trails):
    subtrails = []
    for subtrail in [s for t in trails for s in subtrails_of(t)]:
        if subtrail not in subtrails:
            subtrails.append(subtrail)
    return subtrails


def load_network(network_path):
    with open(network_path) as network_file:
        network = json.load(network_file)
    arcs = [e['id'] for e in network['edges']]
    trails = network['flows']
    subtrails = all_subtrails_of(trails)
    return arcs, subtrails


def solve(name, arcs, subtrails):
    varX = [[
        LpVariable('Ya{}s{}'.format(a, s), cat=LpBinary)
        for s in range(len(subtrails))
    ] for a in range(len(arcs))]

    varY = [
        LpVariable('Ys{}'.format(s), cat=LpBinary)
        for s in range(len(subtrails))
    ]

    model = LpProblem(name, LpMinimize)

    # Objective function (14)
    model += lpSum(varY)

    # Every arc is covered by some subtrail that goes through it (15)
    for a, arc in enumerate(arcs):
        model += lpSum(varX[a][s] for s, subtrail in enumerate(subtrails)
                       if arc in subtrail) == 1

    # If a subtrail is selected to the solution, then all of its arcs must be selected (16)
    for s, subtrail in enumerate(subtrails):
        model += lpSum(varX[a][s] for a, arc in enumerate(arcs)
                       if arc in subtrail) == len(subtrail) * varY[s]

    start = default_timer()
    model.solve(CPLEX_CMD(msg=1, timelimit=3600))
    time = default_timer() - start
    return value(model.objective), time


network_paths = sorted(
    [os.path.join(network_dir, f) for f in os.listdir(network_dir)])
total_networks = len(network_paths)

for i, network_path in enumerate(network_paths):
    network_name = os.path.splitext(basename(network_path))[0]
    print('{} ({}/{})'.format(network_name, i + 1, total_networks))
    arcs, subtrails = load_network(network_path)
    result, time = solve('/networks/zoo_10_12.json', arcs, subtrails)
    print('{};{};{}\n'.format(network_name, result, time))
    with open('cplex_results.csv', 'a') as f:
        f.write('{};{};{}\n'.format(network_name, result, time))
