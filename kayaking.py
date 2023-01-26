n = 2*int(input())
weights = list(map(int, input().split()))
weights.sort()
curr_best = float('inf')


for i in range(n-1):
    for j in range(i+1, n):
        diff = 0
        temp_weights = [weights[x] for x in range(n) if x != i and x != j]
        for m in range ((n-2)//2):
            diff += abs(temp_weights[(m*2)] - temp_weights[(m*2+1)])
        curr_best = min(curr_best, diff)

print(curr_best)