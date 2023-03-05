""""
ID: sarahre1
LANG: PYTHON3
TASK: milk2
"""
import sys
fin = open("milk2.in", "r")
fout = open("milk2.out", "w")
n = int(fin.readline())
times = []
for i in range(n):
    times.append([int(x) for x in fin.readline().split()])
times = sorted(times, key=lambda x: x[0])
sys.stderr.write(str(times))
milking = 0
milk_time = 0
rest_time = 0
last_e = 0
for i in range(n):
    s = int(times[i][0])
    e = int(times[i][1])
    if i == 0:
        milking = e - s
        milk_time = max(milk_time, milking)
    elif s <= last_e:
        if e > last_e:
            milking += e - last_e
    else:
        milk_time = max(milk_time, milking)
        milking = e - s
        # sys.stderr.write("setting rest_time to: "+str(max(rest_time, s - last_e))+'\n')
        rest_time = max(rest_time, s - last_e)
    last_e = max(e, last_e)

fout.write(str(milk_time)+" "+str(rest_time)+'\n')
