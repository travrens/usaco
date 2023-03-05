n, k = (int(x) for x in input().split())
days = [int(x) for x in input().split()]
moonies = 0
sep_cost = (k+1)*2
single_sep = k+1
continued = False
for i in range(n):
    # if last iter
    if i == n-1:
        if not continued:
            # if dist between curr and next < ind, keep going
            moonies += single_sep
            break
        # else end sub
        if continued:
            moonies += abs(days[first] - days[i]) + 1 + k
            break

    if not continued:
        if abs(days[i]-days[i+1])+1+k < sep_cost:
            first = i
            continued = True
        else:
            moonies += single_sep
    if continued:
        if abs(days[i]-days[i+1]) < single_sep:
            continue
        else:
            moonies += abs(days[first]-days[i])+1+k
            continued = False

print(moonies)

# for i in range(n-1):
#     distances.append(abs(days[i]-days[i+1])+1)
#
# continued = False
# for i, dist in enumerate(distances):
#     if not continued and dist+k < sep_cost:
#         first = i
#         continue
#     elif not continued and dist+k > sep_cost:
#         moonies += k+1
#     elif continued and i < len(distances):
#         if dist-1 < k+1:
#             continue
#         else:
#             moonies += abs(days[first]-days[i])+1+k
#     elif continued and i == len(distances):
#         if dist-1 < k+1:
#             moonies += abs(days[first]-days[i+1])+1+k
#         else:
#             moonies += abs(days[first]-days[i])+1+k
#
# print(moonies)
