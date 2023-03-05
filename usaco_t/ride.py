""""
ID: sarahre1
LANG: PYTHON3
TASK: ride
"""
import sys
fin = open("ride.in", "r")
fout = open("ride.out", "w")

comet = fin.readline()
group = fin.readline()
sys.stderr.writelines("comet: "+str(comet))
sys.stderr.writelines("group: "+str(group))
come = [ord(let)-64 for let in comet]
grou = [ord(let)-64 for let in group]
comet = come[0]
group = grou[0]
sys.stderr.writelines("group: "+str(group))
sys.stderr.writelines("comet: "+str(comet))
for l in come:
    comet *= l
comet /= come[0]
for l in grou:
    group *= l
group /= grou[0]
sys.stderr.writelines("group: "+str(group))
sys.stderr.writelines("comet: "+str(comet))
if comet % 47 == group % 47:
    fout.write("GO"+'\n')
else:
    fout.write("STAY"+'\n')
