"""
ID: sarahre1
LANG: PYTHON3
TASK: milk
"""
fin = open("milk.in", "r")
fout = open("milk.out", "w")

n, m = fin.readline().split()
n, m = int(n), int(m)

farmers = []
for i in range(m):
    farmers.append([int(x) for x in fin.readline().split()])
farmers.sort(reverse=True)

cost = 0
while n > 0:
    price, stock = farmers.pop()
    if stock >= n:
        cost += n*price
        break
    else:
        cost += stock*price
        n -= stock

fout.write(str(cost)+"\n")
