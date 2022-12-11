nums = [1,1,3,4,5,5,6,7,7]


# s ={1,2, 3,3} = a set
def Counter(nums):
    counted = {}
    for n in nums:
        if n in counted:
            counted[n] += 1
        else:
            counted[n] = 1
    return counted


# print(Counter(nums))
#
# mydict = {"1": 1, "2": 2, "3": 3}
# mydict["1"] = 10
#
# def printKVs(d):
#     for k, v in d.items():
#         print(k, ": ", v)
#
# keeeys = list(mydict.keys())
# print(keeeys)
# print(mydict.keys(), mydict.values())
#
# printKVs(mydict)
