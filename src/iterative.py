import json
from os import path
from os.path import dirname, abspath
from copy import deepcopy
from collections import deque

root_dir = dirname(dirname(abspath(__file__)))
network_path = path.join(root_dir, 'networks', 'zoo_11_12.json')

with open(network_path) as f:
    network = json.load(f)

flows = deque(network['flows'])
print(flows)
visited = []
solution = []
s_index = 0
s_map = {}

leftovers = deque()

def append_one(flow):
    global s_index
    if flow[0] not in visited:
        visited.append(flow[0])
        solution.append(flow)
        s_map[flow[0]] = s_index
        s_index += 1

while len(flows) > 0:
    flow = flows[0]
    print(flow)

    if len(flow) == 1:
        append_one(flow)
        flows.popleft()

    else:
        h, t = 0, len(flow)
        for j in range(len(flow)):
            if flow[j] in visited:
                h += 1
            else:
                break

        if h < t:
            for j in reversed(range(len(flow))):
                if flow[j] in visited:
                    t -= 1
                else:
                    break

        if h == t:
            flows.popleft()
        elif h == t - 1:
            append_one(flow[h:t])
            flows.popleft()
        elif any(e in visited for e in flow[h:t]):
            leftovers.append(flows.popleft())
        else:
            sol = flow[h:t]
            visited = visited + sol
            solution.append(sol)
            for s in sol:
                s_map[s] = s_index
            s_index += 1
            flows.popleft()

print(solution)
print(leftovers)
