"""
0   1   2

3   4   5

6   7   8
"""
fin = open("tttt.in", "r")
fout = open("tttt.out", "w")
board = fin.readline()[:3]
board += fin.readline()[:3]
board += fin.readline()[:3]

ind_ws = set()
d_ws = set()

def add_w(myset):
    if len(myset) == 3:
        return
    myset = list(map(str,(m for m in myset)))
    myset.sort()
    myset = "".join(myset)
    if len(myset) == 1:
        ind_ws.add(myset)
    else:
        d_ws.add(myset)

for i in range(3):
    myset = {board[i], board[i + 3], board[i + 6]}
    add_w(myset)

    i *= 3
    myset = {board[i + 0], board[i + 1], board[i + 2]}
    add_w(myset)

myset = {board[0], board[4], board[8]}
add_w(myset)

myset = {board[2], board[4], board[6]}
add_w(myset)

fout.write(str(len(ind_ws)) + "\n")
fout.write(str(len(d_ws)))
