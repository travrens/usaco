fin = open("2.in", "r")
fout = open("angry.out", "w")

bales_n = fin.readline()
if bales_n == 1:
    fout.write("1")
    exit(0)
bales = []

for line in fin.readlines():
    bales.append(int(line))

bales.sort()
print(bales)
most_explosions = 0

for i in range(len(bales)):
    exploding = True
    ex_range = 1
    explosions = 1
    print("barrel", bales[i], "explodes first *****")
    j = i
    while exploding and j-1 >= 0:
        if abs(bales[j]-bales[j-1]) <= ex_range:
            print(bales[j - 1], "exploded ***")
            explosions += 1
            ex_range += 1
            print("range is now" ,ex_range, "+")
            j -= 1
        else:
            exploding = False
    print("explosions after left:", explosions)
    exploding = True
    j = i
    ex_range = 1
    while exploding and j+1 <= len(bales) - 1:
        if abs(bales[j]-bales[j+1]) <= ex_range:
            print(bales[j + 1], "exploded ***")
            explosions += 1
            ex_range += 1
            print("range is now", ex_range, "+")
            j += 1
        else:
            exploding = False
    print("explosions after adding right: ", explosions)
    print("before the if: ", most_explosions)
    if explosions > most_explosions:
        most_explosions = explosions
        print("after the if:", most_explosions)

fout.write(str(most_explosions))
