""""
ID: sarahre1
LANG: PYTHON3
TASK: beads
"""
import sys
fin = open("beads.in", "r")
fout = open("beads.out", "w")
n = int(fin.readline())
necklace = fin.readline()[:-1]
necklace = necklace + necklace[:-1]
most = 0
# sys.stderr.write(str(necklace))

for i in range(len(necklace)):
    left = 0
    right = 0
    j = i - 1
    curr = 0
    while j >= 0 and left + right < n:
        if curr != 0 and curr != necklace[j] and necklace[j] != "w":
            break
        else:
            if curr == 0 and necklace[j] != "w":
                curr = necklace[j]
            left += 1
            j -=1

    j = i
    curr = 0
    while j < 2*n-1 and left + right < n:
        if curr != 0 and curr != necklace[j] and necklace[j] != "w":
            break
        else:
            if curr == 0 and necklace[j] != "w":
                curr = necklace[j]
            left += 1
            j += 1
    most = max(left+right, most)
    # prr = f"i: {i} left: {necklace[i-left:i]} right: {necklace[i:i+right+1]} most: {most} \n"
    # sys.stderr.write(prr)
    #print("i:", i, "left", necklace[i-left:i],"right", necklace[i:i+right+1], "most: ",most)
    if most >= n:
        break

fout.write(str(most)+'\n')
# print(most)

