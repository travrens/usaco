from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())
    # EACH COW'S PREFERENCE
    solutions = set()
    cows = [int(x) for x in input().split()]
    if len(cows) == 1:
        print(str(cows[0]))
        continue

    lastlast = cows[0]
    last = cows[1]
    for i in range(2, len(cows)):
        curr = cows[i]
        if curr == last or curr == lastlast:
            solutions.add(int(curr))
        lastlast = last
        last = curr

    solutions = list(solutions)
    if len(solutions) == 0:
        print("-1")
        continue
    solutions.sort()
    mystr = ""
    for s in solutions:
        mystr += str(s) + " "
    mystr = mystr[:-1]
    print(mystr)



