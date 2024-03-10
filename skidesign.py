"""
ID: sarahre1
LANG: PYTHON3
TASK: skidesign
"""
fin = open("skidesign.in", "r")
fout = open("skidesign.out", "w")

n = int(fin.readline())
heights = []
for i in range(n):
    heights.append(int(fin.readline()))
heights.sort()

highest = heights[-1]
lowest = heights[0]
if highest-lowest-17 <= 0:
    fout.write("0\n")
    # print(0, "no diff")
    exit()

final = float('inf')
for i in range(lowest, highest-16):
    cost = 0
    for j in range(len(heights)):
        low = i
        high = i + 17
        curr = heights[j]
        if curr > high:
            # print("adding",(curr-max)**2)
            cost += (curr-high)**2
        elif curr < low:
            cost += (curr-low)**2
    final = min(cost, final)


fout.write(str(final)+"\n")
# print(final, "looped")
