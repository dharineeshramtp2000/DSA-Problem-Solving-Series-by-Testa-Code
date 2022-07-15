def subarrayWithSumK(nums, k):
    sums = {
    0 : 1
    }

    counter = 0

    for idx in range(1, len(nums)):
        nums[idx] += nums[idx - 1]


    for idx, num in enumerate(nums):

        if num - k in sums:
            counter += sums[num - k]

        if num not in sums:
            sums[num] = 0

        sums[num] += 1


    return counter




    
