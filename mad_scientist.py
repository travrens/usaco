# greedy algorithm

fin = open("breedflip.in", "r")
fout = open("breedflip.out", "w")

n_cows = int(fin.readline())
expectation = list(fin.readline())
reality = list(fin.readline())

transformations = 0
started = False

for i in range(n_cows):
    # a doesnt match b
    if expectation[i] != reality[i]:
        if not started:
            started = True
            transformations += 1
    # a matches b
    else:
        started = False


fout.write(str(transformations))
