import math
from collections import defaultdict
n = int(input())
# n = 2
pos_sprays = defaultdict(int)
neg_sprays = defaultdict(int)

patches = [int(x) for x in input().split()]
# patches = [-1, 3]

for i in range(n, 0, -1):
    patch = patches[n-i]
    effectiveness = n-i+1

    for key in pos_sprays.keys():
        patch += (effectiveness-(n - key))*pos_sprays[key]
    for key in neg_sprays.keys():
        patch -= (effectiveness-(n - key)) * neg_sprays[key]

    if patch > 0:
        neg_sprays[i] += patch
    elif patch < 0:
        patch = abs(patch)
        pos_sprays[i] += patch

sprays = 0
sprays += sum(pos_sprays.values())
sprays += sum(neg_sprays.values())
print(sprays)


