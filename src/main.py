import os
import json
from os.path import dirname, abspath, basename
from pprint import pprint
from instance import Instance
from ordered_set import OrderedSet
from timeit import default_timer

root_dir = dirname(dirname(abspath(__file__)))


def main():
    network_dir = os.path.join(root_dir, 'networks')
    solution_dir = os.path.join(root_dir, 'solutions')
    if not os.path.exists(solution_dir):
        os.makedirs(solution_dir)

    network_paths = sorted(
        [os.path.join(network_dir, f) for f in os.listdir(network_dir)])
    for network_path in network_paths:
        solution, time = job(network_path)
        output = {}
        output['solution'] = len(solution)
        output['time'] = time
        output['routes'] = solution
        output_path = os.path.join(solution_dir, basename(network_path))
        with open(output_path, 'w') as output_file:
            json.dump(output, output_file, indent=2)


def job(network_path):
    print('Job: {}'.format(network_path))
    with open(network_path, 'r') as network_file:
        network = json.load(network_file)

    instance = Instance(network['nodes'], network['edges'], network['flows'],
                        network['capacity'])

    start = default_timer()
    solution = flow_fill(instance)
    end = default_timer()

    return solution, end - start


def flow_fill(instance: Instance):
    max_capacity = instance.capacity

    if max_capacity == 1:
        return initial_routes(instance)

    flows = sorted(instance.flows, key=lambda flow: -len(flow))
    routes = []
    leftovers = []
    covered = []
    last_coverage = 0

    while len(set(covered)) != len(instance.edges):
        for f in flows:
            flow = f
            while True:
                route = flow[:max_capacity]
                rest = flow[max_capacity:]

                if len(set(route) - set(covered)) < len(route):
                    leftover = list(OrderedSet(route) - OrderedSet(covered))
                    if leftover:
                        leftovers.append(leftover)
                else:
                    covered = covered + route
                    routes.append(route)

                if len(rest) >= max_capacity:
                    flow = rest
                else:
                    if set(rest) - set(covered):
                        leftover = list(OrderedSet(rest) - OrderedSet(covered))
                        leftovers.append(leftover)
                    break

        flows = sorted(leftovers, key=lambda flow: -len(flow))
        leftovers = []

    return routes


def initial_routes(instance: Instance):
    return [[edge['id']] for edge in instance.edges]


def get_next_edge(edge, instance):
    sorted_flows = sorted(instance.flows, key=lambda flow: -len(flow))
    for flow in sorted_flows:
        last = flow[-1]

        if edge in flow and edge is not last:
            next_index = flow.index(edge) + 1
            return flow[next_index]

    return None


if __name__ == '__main__':
    main()
