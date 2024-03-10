"""
ID: sarahre1
LANG: PYTHON3
TASK: pprime
"""
import math

fin = open("pprime.in", "r")
fout = open("pprime.out", "w")

a, b = [int(x) for x in fin.readline().split()]
pps = []

for n in range(a, b+1):
    str_n = str(n)
    if str_n == str_n[::-1]:
        highest = int(math.sqrt(n))
        prime = True
        if n % 2 != 0:
            for f in range(3, highest+1, 2):
                if n % f == 0:
                    prime = False
                    break
        else:
            continue
        if prime:
            pps.append(str(n)+'\n')

# def loop(n, highest):
#     divisor = 2
#     while divisor <= highest:
#         if n % divisor != 0:
#             divisor += 1
#             for f in range(divisor+1, highest+1, divisor):
def loop():
    for()

out = ""
for x in pps:
    out += x
fout.write(out)
