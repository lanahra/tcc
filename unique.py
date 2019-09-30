import json
from collections import Counter

with open('networks/zoo_11_12.json') as f:
    g = json.load(f)

flows = g['flows']

flattened = [edge for flow in flows for edge in flow]
count = Counter(flattened)

any_unique = list(filter(lambda flow: any(count[edge] == 1 for edge in flow), flows))
print(any_unique)
