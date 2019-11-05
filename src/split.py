def split(ls, k):
    r = []
    for l in ls:
        for i in range(0, len(l), k):
            r.append(l[i:min(i + k, len(l))])
    return r


a = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]]

for k in range(5):
    print(split(a, k + 1))
