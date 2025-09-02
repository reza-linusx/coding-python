def twoSum(nums, target):
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# test the solution
print(twoSum([2, 7, 11, 15], 9))  # should print [0, 1]
