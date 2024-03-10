""""
ID: sarahre1
LANG: PYTHON3
TASK: test
"""
fin = open("test.in", "r")
fout = open("test.out", "w")
inp = sum([int(x) for x in fin.readline().split()])
fout.write(str(inp) + '\n')
fout.close()
