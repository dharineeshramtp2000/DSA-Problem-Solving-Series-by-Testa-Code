def findPivotIndex(nums):
    rightSum = sum(nums)

    leftSum = 0

    for idx, num in enumerate(nums):
        rightSum -= num

        if leftSum == rightSum:
            return idx

        leftSum += num

    return -1
