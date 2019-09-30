from collections import Counter
from itertools import combinations

flows = [[0, 8, 32], [0, 9, 54], [2, 27, 13, 6], [2, 26, 10], [2, 32],
         [2, 30, 47], [3, 54], [8, 32], [11, 32], [12, 54], [13, 5, 19, 1],
         [13, 6], [14, 26, 10], [13, 5, 24], [14, 32], [14, 28, 35], [15, 44],
         [14, 30, 47], [16, 54], [18, 14, 32], [19, 1], [20, 6], [19, 0, 10],
         [20, 4, 17], [22, 41, 32], [22, 44], [22, 42, 47], [23, 54],
         [34, 38, 6], [33, 26, 10], [33, 32], [33, 30, 47], [33, 31, 54],
         [36, 32], [36, 31, 54], [40, 19, 1], [38, 6], [41, 26, 10], [39, 17],
         [41, 32], [42, 47], [43, 54], [45, 46, 32], [46, 32], [48, 7, 1],
         [49, 13, 6], [48, 10], [49, 17], [50, 24], [50, 21, 25], [51, 32],
         [51, 28, 35], [51, 29, 37], [52, 44], [53, 47]]

unique = [
    9, 27, 3, 11, 12, 15, 16, 18, 4, 23, 34, 40, 39, 43, 45, 7, 21, 25, 29, 37,
    52, 53
]

solution = [[0, 8, 32], [9], [2, 27, 13, 6], [3], [11], [12], [5, 19, 1],
            [15, 44], [14, 30], [16], [18], [20, 4], [22, 41], [23], [34, 38],
            [33, 26, 10], [36, 31, 54], [40], [39], [42, 47], [43], [45, 46],
            [48, 7], [49, 17], [50, 24], [21, 25], [51, 28, 35], [29, 37],
            [52], [53]]

print(list(combinations(flows, 2)))
# counter = Counter([e for flow in flows for e in flow])
# unique = [e for e, count in counter.items() if count == 1]