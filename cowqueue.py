fin = open("cowqueue.in", "r")
fout = open("cowqueue.out", "w")

cows = fin.readline()
appts = []

for line in fin.readlines():
    appts.append(list(map(int, line.split())))

appts.sort(key = lambda x: x[0])

time = 0
for appt in appts:
    if time >= appt[0]:
        time += appt[1]
    else:
        time = appt[0]
        time += appt[1]

fout.write(str(time))