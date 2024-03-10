"""
ID: sarahre1
LANG: PYTHON3
TASK: wormhole
"""
fin = open("wormhole.in", "r")
fout = open("wormhole.out", "w")

x_vals = []
y_vals = []
n = int(fin.readline())
partners = [-1]*n
for i in range(n):
    x, y = [int(x) for x in fin.readline().split()]
    x_vals.append(x)
    y_vals.append(y)

next_on_right = [-1]*n
for i in range(n):
    for j in range(n):
        if x_vals[j] > x_vals[i] and y_vals[j] == y_vals[i]:
            if next_on_right[i] == -1:
                next_on_right[i] = j
            if x_vals[next_on_right[i]] > x_vals[j]:
                next_on_right[i] = j
def check_cycle():
    for i in range(n):
        pos = i
        for j in range(n):
            pos = next_on_right[partners[pos]]
            if pos == -1:
                break
        if pos != -1:
            return 1
    return 0

def solve():
    final = 0

    inde = -1
    for i in range(n):
        if partners[i] == -1:
            inde = i
            break

    # print(f"inde={inde}")
    if inde == -1:
        # mystr = ""
        # for i in range(n):
        #     mystr += f"({i}: {partners[i]}),"
        # print(mystr)
        return check_cycle()

    for j in range(inde+1, n):
        if partners[j] != -1:
            continue
        partners[inde] = j
        partners[j] = inde
        final += solve()
        partners[inde] = -1
        partners[j] = -1
    return final


final = solve()
fout.write(str(final)+"\n")


# n = int(fin.readline())
# wormholes = []
# g_ws = set()
# b_ws = set()
# for i in range(n):
#     wormholes.append(tuple(int(x) for x in fin.readline().split()))
#
#
# def travel(curr_wormhole, w_seen):
#     if curr_wormhole in w_seen:
#         # true means infinite loop
#         return [True, w_seen]
#     w_seen.add(curr_wormhole)
#
#     # find possible next wormholes (same y, greater x)
#     possible_next_wormholes = []
#     for wormhole in wormholes:
#         # same y                               # greater x
#         if wormhole[1] == curr_wormhole[1] and wormhole[0] > curr_wormhole[0]:
#             possible_next_wormholes.append(wormhole)
#
#     print(len(possible_next_wormholes))
#     if len(possible_next_wormholes) == 0:
#         # false means not infinite loop
#         return [False, w_seen]
#     # next wormhole is closest
#     possible_next_wormholes.sort()
#     travel(possible_next_wormholes[0], w_seen)
#
#
# final = 0
# for i in range(n):
#     if wormholes[i] in b_ws or wormholes[i] in g_ws:
#         continue
#     w_seen = set()
#     outp = travel(wormholes[i], w_seen)
#     # true means infinite loop
#     if outp [0] == True:
#         for w in outp[1]:
#             b_ws.add(w)
#         final += 1
#     else:
#         for w in outp[1]:
#             g_ws.add(w)
#
# fout.write(str(final)+"\n")


