"""
ID: sarahre1
LANG: PYTHON3
TASK: palsquare
"""
import sys
fin = open("palsquare.in", "r")
fout = open("palsquare.out", "w")

base = int(fin.readline())

def to_base(n, base):
    if n==0:
        return "0"
    num = ""
    while n > 0:
        remainder = n % base
        if remainder < 10:
            num += str(remainder)
        else:
            num += chr(ord("A")-10+remainder)
        n -= remainder
        n /= base
        n = int(n)
        # print(f'num: {num} n: {n}')
    return num[::-1]

final = ""
for i in range(1, 301):
    squared = i*i
    out = to_base(squared, base)
    if str(out) == str(out)[::-1]:
        final += str(to_base(i, base))+" "+str(out)+"\n"

# def to_dec(n, base):
#     result = 0
#     num = str(n)
#     # print("num: "+num)
#     for i in range(len(num)-1, -1, -1):
#         multiplier = int(num[i])
#         # print("i:",i," adding:",multiplier*(base**(len(num)-i-1)))
#         result += multiplier*(base**(len(num)-i-1))
#     return result
#
# def number(quantity):
#     if quantity < 10:
#         return str(quantity)
#     quantity = chr(ord("A")-10+quantity)
#     return quantity


# def find_m(n, base):
#     multiplied = 1
#     i = 0
#     while multiplied <= n:
#         multiplied = multiplied*base
#         i += 1
#     return i-1

# def to_base(n, base):
#     num = ""
#     m = find_m(n, base)
#     for i in range(m, -1, -1):
#         quantity = int(n/base**i)
#         # print(f"n={n}, quantity={quantity}")
#
#         num += number(quantity)
#         n -= quantity*(base**i)
#     return num


# final = ""
# for i in range(1, 301):
#     squared = i*i
#     out = to_base(squared, base)
#     if str(out) == str(out)[::-1]:
#         final += str(to_base(i, base))+" "+str(out)+"\n"

fout.write(final)
