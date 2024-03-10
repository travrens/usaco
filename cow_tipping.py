from collections import deque

fin = open("cowtip.in", "r")
fout = open("cowtip.out", "w")

flips = 0
n = int(fin.readline())
field = []
for i in range(n):
    field.append(list(fin.readline()[:-1]))

q = deque([(n-1, n-1)])
set_q = set([(n-1, n-1)])

def flip(x, y, field):
    for i in range(x+1):
        for j in range(1+y):
            if field[i][j] == '1':
                field[i][j] = '0'
            else:
                field[i][j] = '1'


while (len(q)):
    x, y = q.popleft()
    if field[x][y] == '1':
        flips += 1
        flip(x, y, field)
    
    if(x-1 >= 0 and (x-1, y) not in set_q):
        q.append((x-1, y))
    if(y-1 >= 0 and (x, y-1) not in set_q):
        q.append((x, y-1))


fout.write(str(flips))

# flips = 0
# inverted = False
# for i in range(n-1, -1, -1):
#     # if the corner needs to be flipped then the entire square i x i needs to be flipped i call it inverted so i don't have to go through everything in the square and flip it
#     corner = field[i][i]
#     if corner:
#         flips += 1
#         inverted = not inverted
#
#
#     # checking the next furthest squares, left and above the corner
#     for j in range(i-1, 0, -1):
#         left = field[j][i]
#         right = field[i][j]
#         if inverted:
#             left = not left
#             right = not right
#
#         if left:
#             flips += 1
#             # flipping each square within the rectangle with left as the bottom right corner of the rectangle
#             for k in range(j, -1, -1):
#                 for l in range(i, -1, -1):
#                     field[k][l] = not field[k][l]
#         if right:
#             flips += 1
#             # same as left except switch i and j in the for loops
#             for k in range(i, -1, -1):
#                 for l in range(j, -1, -1):
#                     field[k][l] = not field[k][l]
#
# fout.write(str(flips))


