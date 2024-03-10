fin = open("1.in", "r")
fout = open("max.out", "w")

n = int(fin.readline())
x_inputs = [int(x) for x in fin.readline().split()]
y_inputs = [int(x) for x in fin.readline().split()]

max = 0

for i in range(n-1):
    x1 = x_inputs[i]
    y1 = y_inputs[i]

    for j in range(1, n):
        x2 = x_inputs[j]
        y2 = y_inputs[j]
        currDist = (x2-x1)**2 + (y2-y1)**2
        if (currDist > max): # distance
            max = currDist

fout.write(str(max))