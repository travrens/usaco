import collections

t = int(input())

for _ in range(t):
    print("\n")
    empt = input()
    inp_len, n_cases = (int(x) for x in input().split())
    columns = []
    for i in range(inp_len):
        columns.append(collections.defaultdict(set))
    outs = set()
    for i in range(n_cases):
        case, out = input().split()
        outs.add(out)
        for id, num in enumerate(case):
            columns[id][num].add(out)
    cons = []
    for idx, col in enumerate(columns):
        to_del = []
        print(f"col{idx}: {col}")
        for k, v in col.items():
            # print(f"k: {k}, v: {v}")
            if len(v) > 1:
                to_del.append(k)
        for deller in to_del:
            del(col[deller])
    rest = set()
    for idx, col in enumerate(columns):
        for k, v in col.items():
            for c in v:
                rest.add(c)
    print("rest: ",rest, outs)
# 4
#
# 1 3
# 0 0
# 0 0
# 1 1
#
# 2 4
# 00 0
# 01 1
# 10 1
# 11 1
#
# 1 2
# 0 1
# 0 0
#
# 2 4
# 00 0
# 01 1
# 10 1
# 11 0
