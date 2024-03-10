"""
ID: sarahre1
LANG: PYTHON3
TASK: combo
"""
fin = open("combo.in","r")
fout = open("combo.out","w")

n = int(fin.readline())
# farmer and master combinations
fcom = [int(x) for x in fin.readline().split()]
mcom = [int(x) for x in fin.readline().split()]
combos = set()

# def make_combos(com):
#     for c in com:
#         if c < 3:
#             a_start =
#         if c > n-2:
#     for a in range(fcom[0]-2, fcom[0]+3):

# start with no overlap, max possible # combos
if n <= 5:
    fout.write(str(n*n*n)+"\n")
    quit()
num_coms = (5*5*5)+(5*5*5)

in_range = True
diffs = []

def find_diffs(num):
    myset = set()
    myset.add(num)
    for i in range(1, 3):
        sub = num-i
        add = num+i
        if add > n:
            add = add-n
        if sub < 1:
            sub = n+sub
        myset.add(add)
        myset.add(sub)
    return myset

# check if each digit within 2 of each other
for i in range(3):
    f = fcom[i]
    m = mcom[i]
    setf = find_diffs(f)
    setm = find_diffs(m)
    diffs.append(len(setf.intersection(setm)))

for d in diffs:
    if d == 0:
        fout.write(str((5*5*5)+(5*5*5))+"\n")
        quit()
        break

overlap = 1
for d in diffs:
    overlap *= d
num_coms -= overlap
fout.write(str(num_coms)+"\n")
