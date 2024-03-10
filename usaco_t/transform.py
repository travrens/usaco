"""
ID: sarahre1
LANG: PYTHON3
TASK: transform
"""
# getting inputs
fin = open("transform.in", "r")
fout = open("transform.out", "w")
n = int(fin.readline())
preimage = []
image = []
for _ in range(n):
    preimage.append(list(fin.readline()[:-1]))
for _ in range(n):
    image.append(list(fin.readline()[:-1]))


# singular rotate function
def rot_90(preimage):
    rotated = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(preimage[n - j - 1][i])
        rotated.append(row)
    return rotated


# singular reflection function (only need horizontal)
def reflect(preimage):
    reflected = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(preimage[i][n-j-1])
        reflected.append(row)
    return reflected

# for c in preimage:
#     print(c)
# print('\n')
# check = reflect(preimage)
# for c in check:
#     print(c)

while True:
    ninety = rot_90(preimage)
    if ninety == image:
        fout.write("1")
        break
    one_eighty = rot_90(ninety)
    if one_eighty == image:
        fout.write("2")
        break
    two_seventy = rot_90(one_eighty)
    if one_eighty == image:
        fout.write("3")
        break
    reflected = reflect(preimage)
    if reflected == image:
        fout.write("4")
        break
    n_ref = reflect(ninety)
    o_ref = reflect(one_eighty)
    t_ref = reflect(two_seventy)
    if n_ref == image or o_ref == image or t_ref == image:
        fout.write("5")
        break
    if preimage == image:
        fout.write("6")
        break
    else:
        fout.write("7")
        break
fout.write('\n')
