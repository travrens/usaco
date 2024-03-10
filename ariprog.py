"""
ID: sarahre1
LANG: PYTHON3
TASK: ariprog
"""
from collections import defaultdict
fin = open("ariprog.in", "r")
fout = open("ariprog.out", "w")

n = int(fin.readline())
m = int(fin.readline())

mylist = [0] * (2*m**2+1)
s = set()
for i in range(m+1):
    for j in range(m+1):
        s.add(i**2 + j**2)
        mylist[i**2+j**2] = 1
list_s = list(s)
list_s.sort()
dictionary = defaultdict(list)

# starting number loop
for i in range(len(s)-m+1):
    num1 = list_s[i]
    for j in range(i+1, len(s)-m+2):
        b = list_s[j] - num1
        if b > (2*m**2-num1) // (n-1):
            break
        found = True
        for k in range(2, n):
            if mylist[num1+k*b] != 1:
                found = False
                break
        if found:
            dictionary[b].append(num1)

final = ""
my_keys = list(dictionary.keys())
if len(my_keys) == 0:
    fout.write("NONE"+"\n")
    exit()
my_keys.sort()
for key in my_keys:
    for val in dictionary[key]:
        final += str(val) + " " + str(key) + "\n"

fout.write(final)
