# n_cows = int(input())
# cows = list(input())
#
# trash = 0
#
# s_cows = set(cows)
# if typ not in s_cows or typ not in s_cows:
#     print("0")
#     exit()
#
# for i in range(n_cows - 2):
#     Hs = 0
#     Gs = 0
#     for x in range(i, i+2):
#         if cows[x] == typ:
#             Gs += 1
#         else:
#             Hs += 1
#     for j in range(i + 2, n_cows):
#         if cows[j] == typ:
#             Gs += 1
#         else:
#             Hs += 1
#         if Gs >= 2 and Hs >= 2:
#             break
#         if Gs == 1 or 1 == Hs:
#             trash += 1
#
# print(trash)


n_cows = int(input())
cows = list(input())

trash = 0

for i in range(n_cows):
    typ = cows[i]

    a = 0
    while n_cows > i+a+1 and cows[i+a+1] != typ:
        a += 1
    b = 0
    while i-b-1 >= 0 and cows[i-b-1] != typ:
        b += 1

    trash += (a+1)*(b+1) - 1 - (a > 0) - (b > 0)


print(trash)
