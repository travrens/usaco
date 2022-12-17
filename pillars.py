pillars = [1, 2, 3, 3]
seen = {}
ans = []
def backtracking(pillars, path):
    if all([x == 3 for x in pillars]):
        ans.append([x for x in path])
        return
    if ans and len(path) >= min([len(x) for x in ans]):
        return
    key = str(pillars)
    if key in seen and seen[key] < len(path):
        return
    seen[key] = len(path)
    # if len(path) > 10:
    #     return
    for i in range(len(pillars)):
        if pillars[i] != 3:
            switch(pillars, i, 1)
            path.append(i)
            backtracking(pillars, path)
            path.pop()
            switch(pillars, i, -1)

def switch(pillars, id, delta):
    pillars[id] = change(pillars[id], delta)
    left = (id-1) % len(pillars)
    pillars[left] = change(pillars[left], delta)
    right = (id + 1) % len(pillars)
    pillars[right] = change(pillars[right], delta)

    # if id == 0:
    #     pillars[-1] = change(pillars[-1], delta)
    # else:
    #     pillars[id - 1] = change(pillars[id-1], delta)
    #
    # if id == len(pillars)-1:
    #     pillars[0] = change(pillars[0], delta)
    # else:
    #     pillars[id+1] = change(pillars[id+1], delta)

def change(val, delta):
    new_val = val + delta
    new_val = ((new_val - 1) % 3) + 1
    return new_val

backtracking(pillars, [])
ans.sort(key=len)
print(ans)