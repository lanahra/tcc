from collections import Counter
from pprint import pprint


def to_str(a):
    return ' ' + ' '.join(map(str, a)) + ' '


def is_sublist(a, b):
    return to_str(a) in to_str(b)


def flows_through(f, occurrences_of):
    return sum([occurrences_of[i] for i in f])


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def split(f, k):
    for l in f:
        for c in chunks(l, k):
            yield c


def solve(interfaces, flows, k):
    covered_by = {i: None for i in interfaces}
    occurrences_of = Counter([i for f in flows for i in f])
    unassigned_flows = sorted(
        flows, key=lambda f: (len(f), -flows_through(f, occurrences_of)))
    solution = []
    s = 0

    for flow in unassigned_flows:
        h = 0
        t = 0

        while t < len(flow):
            interface = flow[t]
            sol = covered_by[interface]

            if sol is None:
                t += 1
            elif is_sublist(solution[sol], flow):
                t += len(solution[sol])
                solution[sol] = None
            elif len(flow[h:t]) > 0:
                subflow = flow[h:t]
                solution.append(subflow)
                for i in subflow:
                    covered_by[i] = s
                s += 1
                h = t
            else:
                h += 1
                t = h

        if len(flow[h:t]) > 0:
            subflow = flow[h:t]
            solution.append(subflow)
            for i in subflow:
                covered_by[i] = s
            s += 1

    solution = [s for s in solution if s]
    solution = list(split(solution, k))
    return solution
