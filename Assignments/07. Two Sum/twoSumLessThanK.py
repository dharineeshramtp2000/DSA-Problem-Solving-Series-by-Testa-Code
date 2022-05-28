def twoSumLessThankK(nums, k):
    nums.sort()
    
    i = 0
    j = len(nums) - 1

    maxSum = 0


    while i < j:
        total = nums[i] + nums[j]

        if total < k:
            maxSum = max(maxSum, total)
            print(maxSum)
            i += 1

        else:
            j -= 1

    return -1 if maxSum == 0 else maxSum
