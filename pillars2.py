pillars = [True, False, True, False, True]
ans = []
def backtracking(pillars, path):
    if all(pillars):
        ans.append([x for x in path])
        return
    if len(path) > 10:
        return
    for i in range(len(pillars)):
        if not pillars[i]:
            switch(pillars, i)
            path.append(i)
            backtracking(pillars, path)
            path.pop()
            switch(pillars, i)

def switch(pillars, id):
    pillars[id] = not pillars[id]
    if id == 0:
        pillars[id-1] = not pillars[id-1]
    else:
        pillars[id-1] = not pillars[id-1]
    if id == len(pillars)-1:
        pillars[0] = not pillars[0]
    else:
        pillars[id+1] = not pillars[id+1]
backtracking(pillars, [])
ans.sort(key=len)
print(ans)