"""
ID: sarahre1
LANG: PYTHON3
TASK: barn1
"""
fin = open("barn1.in", "r")
fout = open("barn1.out", "w")

m,s,c = [int(x) for x in fin.readline().split()]
occupied = []
for i in range(c):
    occupied.append(int(fin.readline()))
occupied.sort()

gaps = []
for i in range(c-1):
    gaps.append(occupied[i+1]-occupied[i]-1)
gaps.sort()

outp = occupied[-1]-occupied[0]+1
for i in range(m-1):
    if len(gaps)>0:
        outp -= gaps.pop()
    else:
        break

fout.write(str(outp)+"\n")
