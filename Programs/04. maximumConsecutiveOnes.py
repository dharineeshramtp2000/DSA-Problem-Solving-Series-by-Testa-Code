def maxConsecutiveOnes(nums):
    maxLength = 0

    i = 0

    while i < len(nums):
        if nums[i] == 0:
            i += 1
            continue

        j = i

        while j < len(nums) and nums[j] == 1:
            j += 1

        maxLength = max(maxLength, j - i)

        i = j

    return maxLength





def maxConsecutiveOnes(nums):
    onesSeen = 0

    maxLength = 0

    for num in nums:
        if num == 0:
            onesSeen = 0

        else:
            oneSeen += 1
            maxLength = max(maxLength, onesSeen)

    return maxLength



    
