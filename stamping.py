t = int(input())

for _ in range(t):
    input()
    n = int(input())
    blank_grid = ["."]*n
    grid = []
    for i in range(n):
        grid.append(input())
    stamp = ""
    k = int(input())
    for i in range(k):
        stamp += input()
    # check if stamp inside, check top left and bottom right
    if k > n:
        print("NO")
        continue
    for i in range(n-k+1):
        string = ""
        for j in range(k):
            string.append(grid[i][i:k+1])
        for j in range(4):
            if stamp == string:
                continue
            else:
                stamp = stamp[-(k-1):]
