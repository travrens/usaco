import collections

fin = open("1.in", "r")
fout = open("lineup.out", "w")

types = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]

n_cons = int(fin.readline())
cons = []

for p in range(n_cons):
    temp = fin.readline().split()
    temp = [temp[0], temp[-1]]
    temp.sort()
    cons.append(temp)

print(cons)
adj = collections.defaultdict(list)
for con in cons:
    adj[con[0]].append(con[1])
    adj[con[1]].append(con[0])

for k,v in adj:
    if

# def runthrucows(current_type):
#     if current_type >= 7:
#         return 0
#     else:
#         return current_type + 1
#
#
#
# def solve(i, current_lineup, next_type):
#     # print("i: "+str(i))
#     # print(current_lineup)
#     current_lineup += types[next_type] + " "
#     next_type = runthrucows(next_type)
#     if i >= 7:
#         return current_lineup + types[next_type] + " "
#     for x in range(7):
#         next_type = runthrucows(next_type)
#         combinations.append(solve(i + 1, current_lineup, next_type))
#     return combinations
#
# combinations = []
# nexxxxt = 0
# for j in range(7):
#     nexxxxt = runthrucows(nexxxxt)
#     combinations.append(solve(0, "", nexxxxt))
#
# for combo in combinations:
#     print(combo)
#
#
# chosen = [False] * 8
# res = []
# def search(permutation):
#     if len(permutation) == 8:
#         res.append(permutation[:])
#     else:
#         for i in range(8):
#             # print(i)
#             # print(chosen)
#             if (chosen[i]):
#                 continue
#             chosen[i] = True
#             permutation.append(types[i])
#             search(permutation)
#             chosen[i] = False
#             permutation.pop()
#
# search([])
# print(res)
