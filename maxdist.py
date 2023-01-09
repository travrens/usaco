# usacoguide basic complete search

n = int(input())
x_coors = list(map(int, input().split()))
y_coors = list(map(int, input().split()))

res = 0
for i in range(n-1):
    for j in range(i+1, n):
        coor1 = x_coors[i], y_coors[i]
        coor2 = x_coors[j], y_coors[j]
        res = max(((coor1[0]-coor2[0])**2 + (coor1[1]-coor2[1])**2),res)
print(res)
