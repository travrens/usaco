"""
ID: sarahre1
LANG: PYTHON3
TASK: crypt1
"""
fin = open("crypt1.in", "r")
fout = open("crypt1.out", "w")

n = int(fin.readline())
comparison = set(fin.readline().split())
digits = [int(x) for x in comparison]
final = 0
'''
123
x45
'''
# 1
for a in range(n):
    #2
    for b in range(n):
        #3
        for c in range(n):
            #4
            for d in range(n):
                #5
                for e in range(n):
                    # put all numbers in the equation into a string to iterate to compare if in available digits
                    mystring = ""
                    multiplier1 = int(str(digits[a])+str(digits[b])+str(digits[c]))
                    multiplier2 = int(str(digits[d])+str(digits[e]))
                    # add the multipliers
                    mystring += str(digits[a])+str(digits[b])+str(digits[c])+str(digits[d])+str(digits[e])
                    # check if output and partial outputs right length
                    if len(str(multiplier1*multiplier2))==4 and len(str(multiplier1*digits[d]))==3 and len(str(multiplier1*digits[e]))==3:
                        # if yes, add all to string
                        mystring += str(multiplier1*multiplier2)+str(multiplier1*digits[d])+str(multiplier1*digits[e])
                    else:
                        continue
                    # compare mystring and comparison
                    match = True
                    for l in mystring:
                        if l not in comparison:
                            match = False
                            break
                    if match:
                        final += 1
fout.write(str(final)+"\n")
