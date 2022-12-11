fin = open("notlast.in", "r")
fout = open("notlast.out", "w")

result = None
n = int(fin.readline())
cows = {"Bessie":0, "Elsie":0, "Daisy":0, "Gertie":0, "Annabelle":0, "Maggie":0, "Henrietta":0}

for i in range(n):
    cow, milk = fin.readline().split()
    milk = int(milk)
    cows[cow] += milk

cow_values = list(set(cows.values()))
cow_values.sort()
result_cows = []

if len(cow_values) > 1:
    second_min = cow_values[1]
    for k, v in cows.items():
        if v == second_min:
            result_cows.append(k)
            if len(result_cows) > 1:
                result = "Tie"
                break
    if result != "Tie":
        result = result_cows[0]
else:
    result = "Tie"


fout.write(result)
