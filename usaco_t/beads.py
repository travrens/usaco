""""
ID: sarahre1
LANG: PYTHON3
TASK: beads
"""
#           .=     ,        =.
#   _  _   /'/    )\,/,/(_   \ \
#    `//-.|  (  ,\\)\//\)\/_  ) |
#    //___\   `\\\/\\/\/\\///'  /
# ,-"~`-._ `"--'_   `"""`  _ \`'"~-,_
# \       `-.  '_`.      .'_` \ ,-"~`/
#  `.__.-'`/   (-\        /-) |-.__,'
#    ||   |     \O)  /^\ (O/  |
#    `\\  |         /   `\    /
#      \\  \       /      `\ /
#       `\\ `-.  /' .---.--.\
#         `\\/`~(, '()      ('
#          /(O) \\   _,.-.,_)
#         //  \\ `\'`      /
#        / |  ||   `""""~"`
#      /'  |__||
#            `o
import sys
fin = open("beads.in", "r")
fout = open("beads.out", "w")
n = int(fin.readline())
string = fin.readline()
most = 0

forward = 1
backward = 1

for i in range(n):
    # forward
    # case r
    if string[i] == "r":
        curr = "r"
        not_curr = "b"
    # case b
    elif string[i] == "b":
        curr = "b"
        not_curr = "r"
    # case w
    else:
        # while white, set to the next
        for x in range(i+1, n):
            if string[x] == "w":
                continue
            else:
                curr = string[x]
                found = True
        if not found:
            for x in range(i):
                if string[x] == "w":
                    continue
                else:
                    curr = string[x]
                    found = True
        if not found:
            most = n
            break
        if curr == "r":
            not_curr = "b"
        else:
            not_curr = "r"
    # forward check
    if forward >= 2:
        forward -= 1
    else:
        forward = 1
        for j in range(i+1, i+n):
            if j == n:
                j = 0
            if string[j] == not_curr:
                break
            else:
                forward += 1
    # backward
    string = string[::-1]
    i = -i - 1
    if string[i] == "r":
        curr = "r"
        not_curr = "b"
    # case b
    elif string[i] == "b":
        curr = "b"
        not_curr = "r"
    # case w
    else:
        # while white, set to the next
        for x in range(i+1, i+n):
            if x == n:
                x = 0
            if string[x] == "w":
                continue
            else:
                curr = string[x]
        if curr == "r":
            not_curr = "b"
        else:
            not_curr = "r"
    if backward >= 2:
        backward -= 1
    else:
        backward = 1
        for j in range(i + 1, i + n):
            if j == n:
                j = 0
            if string[j] == not_curr:
                break
            else:
                backward += 1
    if forward + backward > most:
        most = forward + backward
    if most >= n:
        break

fout.write(str(most)+'\n')
