# basic complete search

fin = open("pails.in", "r")
fout = open("pails.out", "w")

x, y, z = map(int, fin.readline().split())
# print(x," ",y," ",z)
# print("\n")

# def solve(x, y, z):
#     x_remainder = z%x
#     y_remainder = z%y
#     print("x_r: ",x_remainder)
#     print("y_r: ", y_remainder)
#     while y_remainder > x:
#         y_remainder -= x
#     print("y_r after while loop: ", y_remainder)
#     return min(x_remainder, y_remainder)
#
# max_fill = z - solve(x, y, z)
# print(max_fill)

visited = {}

def solve(x, y, z):
    if z in visited:
        return visited[z]
    ret = 0
    if z >= x:
        ret = x + solve(x, y, z - x)
    if z >= y:
        ret = max(ret, y + solve(x, y, z - y))
    visited[z] = ret
    return ret

fout.write(str(solve(x, y, z)))
# print(str(solve(x, y, z)))

#
# 17, [50-17=33] solve(17, 18, 33)
#    17, 33-17=16 solve(17, 18, 16)
#    18, 33-18=15 solve(17, 18, 15)
#    ret = 18
# ret = 17 + 18 = 35
# 18, [50-18=32] solve(17, 18, 32)
#     17, 32-17=15 solve(17, 18, 15)
#     ret = x + 0
#     ret = x
#     ret = 17
#     18, 32-18=14 solve(17, 18, 14)
#     ret = y + 0
#     ret = y
#     ret = 18
# ret = 18 + 18 = 36