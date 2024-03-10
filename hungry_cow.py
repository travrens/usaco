n, t = (int(x) for x in input().split())
eaten = 0
day = 1

for i in range(n):
    d, b = (int(x) for x in input().split())
    if day < d:
        day = d

    if day + b < t:
        day += b
        eaten += b
    elif day + b == t:
        eaten += b
        break
    else:
        eaten += b - abs((day+b)-t) + 1
        break
print(eaten)
