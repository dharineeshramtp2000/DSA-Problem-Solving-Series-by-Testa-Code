def moveZeroes(nums):
    nonZeroIndex = 0


    for num in nums:
        if num == 0:
            continue

        nums[nonZeroIndex] = num
        nonZeroIndex += 1


    while nonZeroIndex < len(nums):
        nums[nonZeroIndex] = 0
        nonZeroIndex += 1

    return nums
