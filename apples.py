apples = list(map(int, input().split()))
n = len(apples)

def solve(w1, w2, i):
    print(f"enter: {w1}, {w2}, {i}")
    if i >= n:
        print("return: ", abs(w1-w2))
        return abs(w1-w2)
    left = solve(w1 + apples[i], w2, i+1)
    right = solve(w1, w2 + apples[i], i+1)
    ret = min(left, right)
    print(f"left: {left}, right: {right}, ret: {ret}")
    return ret

print(solve(0, 0, 0))

'''
3 2 7 
enter: 0 0 0
enter: 3, 0, 1
enter: 5, 0, 2
enter: 12, 0, 3
return: 12
enter: 5, 7, 3
return: 2
left: 12, right: 2, ret: 2
enter: 3, 2, 2
enter: 10, 2, 3
return: 8
enter: 3, 9, 3
return: 6
left: 8, right: 6, ret: 6
left: 2, right: 6, ret: 2
'''
