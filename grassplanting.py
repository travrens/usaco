import collections

fin = open("planting.in", "r")
fout = open("planting.out", "w")

n_fields = int(fin.readline())
fields = collections.defaultdict(list)

for i in range(n_fields - 1):
    u, v = fin.readline().split()
    fields[u].append(v)
    fields[v].append(u)

ret = 0
for k, v in fields.items():
    ret = max(ret, len(v))

ret += 1
fout.write(str(ret))

# def DFS(fields, u, visited):
#     if u in visited:
#         return
#     print("before u:", u)
#     visited.add(u)
#     for neighbor in fields[u]:
#         if neighbor not in visited:
#             DFS(fields, neighbor, visited)
#     print("after u:", u)
#
# visited = set()
# for field in fields:
#     DFS(fields, field, visited)
