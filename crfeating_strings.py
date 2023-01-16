# from typing import List
#
# # crfeate = list(input())
# crfeate = ['a', 'a', 'b', 'a', 'c']
# n = len(crfeate)
#
# OUTP = set()
# used = [False] * n
#
#
# def permutate(cur: List[str]):
#     print(f"enter: used={used}, cur={cur}")
#     if len(cur) == n:
#         OUTP.add(''.join(cur))
#         return
#     for i in range(n):
#         if not used[i]:
#             cur.append(crfeate[i])
#             used[i] = True
#             permutate(cur)
#             used[i] = False
#             cur.pop()
#
#
# permutate([])
# OUTP = list(OUTP)
# OUTP.sort()
#
# print(len(OUTP))
# for combo in OUTP:
#     print(combo)
#


s = input()
perms = []
chars_count = [0] * 26

def search(curr_perm):
    print(f"enter: {curr_perm}, chars_count={chars_count}")
    if len(curr_perm) == len(s):
        print(f"add {curr_perm}")
        perms.append(curr_perm)
        return
    for i in range(26):
        if chars_count[i] > 0:
            chars_count[i] -= 1
            search(curr_perm+chr(ord('a')+i))
            chars_count[i] += 1

for c in s:
    chars_count[ord(c)-ord("a")] += 1
search("")
print(len(perms))
for perm in perms:
    print(perm)

alphabet = {}
for i in range(26):
    alphabet[chr(ord("a")+i)] = 0

for k,v in alphabet.items():
    print(k, v)