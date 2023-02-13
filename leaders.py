n = int(input())
lineup = input()
lists = list(map(int, input().split()))

first_G = ""
first_H = ""
last_G = ""
last_H = ""
# the index of last are index, not position
if lineup[n-1] == "G":
    last_G = n-1
    # set other one, going backwards thru lineup
    n_dupe = n-2
    while last_H == "":
        if lineup[n_dupe] == "H":
            last_H = n_dupe
            break
        else:
            n_dupe -= 1
else:
    last_H = n-1
    # set other one, going backwards thru lineup
    n_dupe = n-2
    while last_G == "":
        if lineup[n_dupe] == "G":
            last_G = n_dupe
            break
        else:
            n_dupe -= 1
if lineup[0] == "G":
    first_G = 0
    for i in range(1, last_H+1):
        if lineup[i] == "H":
            first_H = i
            break
else:
    first_H = 0
    for i in range(1, last_G+1):
        if lineup[i] == "G":
            first_G = i
            break
# first check leader status by "do they have everyone in their breed"
g_leaders = set()
h_leaders = set()
if lists[first_G] >= last_G:
    g_leaders.add(first_G)
if lists[first_H] >= last_H:
    h_leaders.add(first_H)
# now check leader status by "do they have another leader"
combos = (len(g_leaders) * len(h_leaders))
if len(g_leaders) > 0:
    # if first_H < first_G:
    for i in range(first_H, first_G):
        if lineup[i] == "H":
            if i in h_leaders:
                continue
            if first_G < lists[i]:
                combos += 1
if len(h_leaders) > 0:
    # if first_G < first_H:
    for i in range(first_G, first_H):
        if lineup[i] == "G":
            if i in g_leaders:
                continue
            if first_H < lists[i]:
                combos += 1
# for i in range(n):
#     if lineup[i] == "H":
#         if i in h_leaders:
#             continue
#         if i < first_G:
#             for j in range(i+1, lists[i]):
#                 if j in g_leaders:
#                     combos += 1
#     else:
#         if i in g_leaders:
#             continue
#         if i < first_H:
#             for j in range(i+1, lists[i]):
#                 if j in h_leaders:
#                     combos += 1
print(combos)
