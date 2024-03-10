"""
ID: sarahre1
LANG: PYTHON3
TASK: namenum
"""
import sys

fin = open("namenum.in", "r")
fout = open("namenum.out", "w")

fopen = open("dict.txt", "r")
s_names = set()
lines = fopen.readlines()
for line in lines:
    s_names.add(line[:-1])

# for pycharm
# serial = fin.readline()
# for usaco grader
serial = fin.readline()[:-1]

dictionary = {
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J','K','L'],
    '6': ['M','N','O'],
    '7': ['P','R','S'],
    '8': ['T','U','V'],
    '9': ['W','X','Y']
}

outs = []
# def recursion(i, curr_name):
#     if i < len(serial) and len(curr_name) == len(str(serial)):
#         possibilities = dictionary[serial[i]]
#
#         if curr_name[i] in possibilities:
#             if i == len(curr_name)-1:
#                 outs.append(curr_name)
#                 return
#             recursion(i + 1, curr_name)
#     else:
#         return
#
#
# recursion(0, serial, )

def recursion(i, inp, curr):
    if i == len(inp):
        outs.append(curr)
        return
    possibilities = dictionary[inp[i]]
    for l in possibilities:
        recursion(i+1, inp, curr+l)

recursion(0, serial, '')

final_outs = []
for name in outs:
    if name in s_names:
        final_outs.append(name)
final_outs.sort()

if not final_outs:
    fout.write("NONE\n")
for name in final_outs:
    fout.write(name+'\n')

