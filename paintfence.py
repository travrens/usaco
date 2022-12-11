fin = open("paint.in", "r")
fout = open("paint.out", "w")

john = list(map(int, fin.readline().split()))
cow = list(map(int, fin.readline().split()))

if john[0] > cow[0]:
    john, cow = cow, john

painted = 0
if john[1] < cow[0]:
    painted = john[1] - john[0] + cow[1] - cow[0]
else:
    painted = max(cow[1], john[1]) - john[0]
#
# if john[0] < cow[0]:
#     range_min = john[0]
#     range_second_min = cow[0]
#     min = john
#     second_min = cow
# else:
#     range_min = cow[0]
#     range_second_min = john[0]
#     min = cow
#     second_min = john
# if min[1] < range_second_min:
#     gap = True
# else:
#     gap = False
#
# if gap:
#     seg1 = (min[1] - range_min)
#     seg2 = (second_min[1] - range_second_min)
#     if seg1 == 0:
#         seg1 = 1
#     if seg2 == 0:
#         seg2 = 1
#     painted = seg1 + seg2
# else:
#     if min[1] > second_min[1]:
#         painted = min[1] - range_min
#     else:
#         painted = second_min[1] - range_min

fout.write(str(painted))