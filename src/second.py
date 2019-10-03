from random import shuffle

visited = []
solution = []
s_index = 0
s_map = {}
leftovers = []


def to_str(a):
    return ' ' + ' '.join(map(str, a)) + ' '


def is_sublist(a, b):
    return to_str(a) in to_str(b)


def has_any_sublist(flow):
    for e in flow:
        if e in visited:
            index = s_map[e]
            s = solution[index]
            if is_sublist(s, flow):
                return True
    return False


def solve(flows):
    global visited
    global solution
    global s_index
    global s_map
    global leftovers
    visited = []
    solution = []
    s_index = 0
    s_map = {}
    leftovers = []

    for flow in flows:
        h, t = 0, len(flow)
        has_sublists = False

        if has_any_sublist(flow):
            has_sublists = True

        i = 0
        while i < len(flow):
            if flow[i] in visited:
                index = s_map[flow[i]]
                s = solution[index]

                if has_sublists and is_sublist(s, flow):
                    visited = [v for v in visited if v not in s]
                    solution[index] = []
                    i += len(s)
                elif has_sublists and (flow[i] == s[0] or flow[i] == s[-1]):
                    visited.remove(flow[i])
                    solution[index].remove(flow[i])
                    i += 1
                else:
                    i += 1
                    h += 1
            else:
                break

        if h < t:
            i = len(flow) - 1
            while i > 0:
                if flow[i] in visited:
                    index = s_map[flow[i]]
                    s = solution[index]

                    if has_sublists and is_sublist(s, flow):
                        visited = [v for v in visited if v not in s]
                        solution[index] = []
                        i -= len(s)
                    elif has_sublists and (flow[i] == s[0]
                                           or flow[i] == s[-1]):
                        visited.remove(flow[i])
                        solution[index].remove(flow[i])
                        i -= 1
                    else:
                        i -= 1
                        t -= 1
                else:
                    break

        if any(e in visited for e in flow[h:t]):
            leftovers.append(flow)
        else:
            sol = flow[h:t]
            visited = visited + sol
            solution.append(sol)
            for s in sol:
                s_map[s] = s_index
            s_index += 1

    enum = {f[0]: f[1] for f in enumerate(solution) if len(f[1]) > 0}
    return list(filter(lambda x: len(x) > 0, solution)), leftovers, enum
