""""
ID: sarahre1
LANG: PYTHON3
TASK: gift1
"""
import sys
import collections
fin = open("gift1.in", "r")
fout = open("gift1.out", "w")
n = int(fin.readline())
accts = collections.defaultdict()

for _ in range(n):
    accts[fin.readline()[:-1]] = 0
for _ in range(n):
    giver = fin.readline()[:-1]
    amt, ppl = map(int, fin.readline()[:-1].split())
    sys.stderr.write("amt: "+str(amt)+" ppl: "+str(ppl)+'\n')
    if amt == 0 or ppl == 0:
        for i in range(ppl):
            fin.readline()
        continue
    giving = int(amt/ppl)
    accts[giver] += int((amt % ppl) - amt)
    for _ in range(ppl):
        givee = fin.readline()[:-1]
        sys.stderr.write("givee: "+givee+"amt: "+str(giving)+'\n')
        accts[givee] += giving
        # sys.stderr.write("gave"+'\n')
for k, v in accts.items():
    fout.write(k+" "+str(v)+'\n')
