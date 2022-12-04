num = [45, 2, 1, 6, 8, 9, 1]

def BubbleSort(nums):
    swapping = True
    swapped = False
    while swapping:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True
            else:
                continue
        if swapped:
            swapped = False
            continue
        else:
            return nums


print("before: ", num)
num = BubbleSort(num)
print("after bubble sort: ", num)

num = [45, 2, 1, 6, 8, 9, 1]


def MergeSort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums)//2
    L = nums[:mid]
    R = nums[mid:]

    sortd_L = MergeSort(L)
    sorted_R = MergeSort(R)
    ret = []

    i = j = 0

    while i < len(L) and j < len(R):
        if sortd_L[i] <= sorted_R[j]:
            ret.append(sortd_L[i])
            i += 1
        else:
            ret.append(sorted_R[j])
            j += 1

    while i < len(L):
        ret.append(sortd_L[i])
        i += 1

    while j < len(R):
        ret.append(sorted_R[j])
        j += 1

    return ret


print("before: ", num)
ret = MergeSort(num)
print("after merge sort: ", ret)
