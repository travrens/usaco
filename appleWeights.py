# 5
# 3 2 7 4 1

n_apples = 5
apples = [3,2,7,4,1]

def solve(i, w1, w2):
    if i == n_apples:
        return abs(w2-w1)
    return min(solve(i+1, w1 + apples[i], w2), solve(i+1, w1, w2 + apples[i]))

print(solve(0,0,0))