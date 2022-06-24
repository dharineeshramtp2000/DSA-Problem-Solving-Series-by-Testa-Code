def containsDuplicate(nums, k):

    hashTable = {}

    for idx, num in enumerate(nums):

        if num in hashTable and (idx - hashTable[num]) <= k:
            return True

        hashTable[num] = idx

    return False

def containsDuplicate(nums, k):

    previousKElements = set()

    for idx, num in enumerate(nums):

        if num in previousKElements:
            return True

        previousKElements.add(num)

        if len(previousKElements) > k:
            previousKElements.remove(nums[idx - k])

    return False
