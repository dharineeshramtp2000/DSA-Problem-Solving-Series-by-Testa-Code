def findShortestSubArray(nums):

    start = {}
    end = {}
    counter = {}

    degree = 0

    for idx, num in enumerate(nums):

        if num not in start:
            start[num] = idx
            counter[num] = 0

        counter[num] += 1
        end[num] = idx

        degree = max(degree, counter[num])


    shortestSubArrayLength = len(nums)


    for num in counter.keys():

        if counter[num] == degree:
            shortestSubArrayLength = min(shortestSubArrayLength, end[num] - start[num] + 1)

    return shortestSubArrayLength
