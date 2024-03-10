"""
ID: sarahre1
LANG: PYTHON3
TASK: milk3
"""
fin = open("milk3.in", "r")
fout = open("milk3.out", "w")

capacities = [int(x) for x in fin.readline().split()]
visited = set()
my_cs = set()

def pour(buckets):
    mytup = tuple(buckets)
    if mytup in visited:
        return
    else:
        visited.add(mytup)
        if buckets[0] == 0:
            my_cs.add(buckets[-1])

        # pourer
        for i in range(3):
            # if pourer empty
            if buckets[i] == 0:
                continue
            # pour into
            left = (i+1)%3
            right = (i + 2) % 3

            for indexx in [left, right]:
                capacity = capacities[indexx]
                curr = buckets[indexx]
                if capacity >= curr:
                    space = capacity - curr
                    vol = buckets[i]
                    # save
                    src = buckets[i]
                    dest = buckets[indexx]
                    # can pour all
                    if vol <= space:
                        buckets[indexx] += vol
                        buckets[i] = 0
                    else:
                        buckets[i] -= space
                        buckets[indexx] = capacity
                    pour(buckets)
                    # restore
                    buckets[i] = src
                    buckets[indexx] = dest


pour([0, 0, capacities[2]])

sol = list(my_cs)
sol.sort()
mystr = ""
for s in sol:
    mystr += str(s) + " "

fout.write(mystr[:-1]+"\n")
