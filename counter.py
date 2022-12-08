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


print(Counter(nums))