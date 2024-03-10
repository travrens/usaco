"""
ID: sarahre1
LANG: PYTHON3
TASK: numtri
"""
fin = open("numtri.in", "r")
fout = open("numtri.out", "w")

r = int(fin.readline())
pyramid = []
for i in range(r):
    pyramid.append(list(int(x) for x in fin.readline().split()))
highest = 0

for y in range(r-2, -1, -1):
    for x in range(y+1):
        pyramid[y][x] += max(pyramid[y+1][x], pyramid[y+1][x+1])

fout.write(str(pyramid[0][0])+"\n")
