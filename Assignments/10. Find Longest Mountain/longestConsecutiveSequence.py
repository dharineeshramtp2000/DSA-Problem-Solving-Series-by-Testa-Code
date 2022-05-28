def longestConsecutive(nums):
    memory = {}

    for num in nums:
        memory[num] = False

    longestLength = 0

    for num in nums:
        if memory[num]:
            continue
        memory[num] = True
        leftSize = findLength(num - 1, -1, memory)
        rightSize = findLength(num + 1, 1, memory)

        longestLength = max(longestLength, leftSize + rightSize + 1)
    return longestLength


def findLength(startNumber, step, memory):
    count = 0

    while startNumber in mem:
        count += 1
        memory[startNumber] = True
        startNumber += step

    return count
