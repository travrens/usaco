""""
ID: sarahre1
LANG: PYTHON3
TASK: friday
"""
import sys

def Month(month):
    if month == "jan":
        return 31
    if month == "mar":
        return 31
    if month == "may":
        return 31
    if month == "jul":
        return 31
    if month == "aug":
        return 31
    if month == "oct":
        return 31
    if month == "dec":
        return 31
    elif month == "sep":
        return 30
    elif month == "apr":
        return 30
    elif month == "jun":
        return 30
    elif month == "nov":
        return 30


fin = open("friday.in", "r")
fout = open("friday.out", "w")
n = int(fin.readline())
sys.stderr.write("n: "+str(n))
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
# 0th is monday:
thirteens = [0] * 7
day = 0
for yr in range(1900, 1900+n):
    sys.stderr.write("in loop")
    if yr % 4 == 0 and yr % 100 != 0:
        leap = True
    elif yr % 400 == 0:
        leap = True
    else:
        leap = False
    for mon in months:
        if mon == "feb":
            if leap:
                days = 29
            else:
                days = 28
        else:
            days = Month(mon)
        days -= 12
        day += 12
        thirteens[day % 7] += 1
        day += days

for i in range(5, 7):
    fout.write(str(thirteens[i]) + " ")
for i in range(0, 4):
    fout.write(str(thirteens[i]) + " ")
fout.write(str(thirteens[4]))
fout.write('\n')
