"""
ID: sarahre1
LANG: PYTHON3
TASK: dualpal
"""
import sys

fin = open("dualpal.in", "r")
fout = open("dualpal.out", "w")

n, s = fin.readline().split()
n, s = int(n), int(s)
def to_base(s, base):
    if s==0:
        return "0"
    num = ""
    while s > 0:
        remainder = s % base
        num += str(remainder)
        s -= remainder
        s /= base
        s = int(s)
        # print(f'num: {num} n: {n}')
    return num[::-1]

final = []
while True:
    s += 1
    pals = 0
    for i in range(2, 11):
        res = to_base(s, i)
        res = str(res)
        if res == res[::-1] and res[0] != "0":
            pals += 1
    if pals >= 2:
        final.append(s)
    if(len(final) >= n):
        break

final.sort()
pr = ""
for f in final:
    pr += str(f)
    pr += "\n"
fout.write(pr)
