n, target = list(map(int, input().split()))
nums = list(map(int, input().split()))
dict_nums = {}

for i in range(n):
    num = nums[i]
    if target - num in dict_nums:
        print(dict_nums[target - num]+1, i+1)
        break
    dict_nums[num] = i
