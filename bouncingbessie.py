mylist = [int(x) for x in input().split()]
n = mylist[0]
s = mylist[1]
power = 1
# LEFT -1  1 RIGHT
direction = 1
# TUPLES LOCATION, DIRECTION, POWER
visited = set()
locations = []
for i in range(n):
    myinp = [int(x) for x in input().split()]
    locations.append(myinp)

def switch(dire):
    return dire*-1


broken = 0
targets_broken = set()

if locations[s][0] == 0:
    power += locations[s][1]
    direction = switch(direction)
else:
    if locations[s][1] <= power:
        targets_broken.add(s)
        broken += 1

next_location = s
while True:
    next_location += power*direction
    if next_location < 0 or next_location >= len(locations):
        break

    cuee = tuple([next_location, power, direction])
    if cuee in visited:
        break
    visited.add(cuee)
    what = locations[next_location][0]
    val = locations[next_location][1]
    # 0 is jump pad
    if what == 0:
        power += val
        direction = switch(direction)
    else:
        if next_location not in targets_broken:
            if val <= power:
                targets_broken.add(next_location)
                broken += 1

print(str(broken))



