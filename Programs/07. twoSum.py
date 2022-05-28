def twoSum(nums, target):
    seen = set()

    for num in nums:

        remainingSum = target - num

        if remainingSum in seen:
            return [num, remainingSum]

        seen.add(num)

    return []
