from pprint import pformat


class Instance:
    def __init__(self, nodes, edges, flows, capacity):
        self.nodes = nodes
        self.edges = edges
        self.flows = flows
        self.capacity = capacity

    def __str__(self):
        return 'Instance({})'.format(
            pformat({
                'nodes': self.nodes,
                'edges': self.edges,
                'flows': self.flows,
                'capacity': self.capacity
            }))
