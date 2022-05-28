def evenOddArrange(nums):
    evenIdx = 0
    oddIdx = 1

    while evenIdx < len(nums) and oddIdx < len(nums):

        evenIdxNumber = nums[evenIdx]
        oddIdxNumber = nums[oddIdx]

        if isOdd(evenIdxNumber) and isEven(oddIdxNumber):
            swap(evenIdx, oddIdx, nums)
            evenIdx += 2
            oddIdx += 2

        elif isEven(evenIdxNumber):
            evenIdx += 2

        elif isOdd(oddIdxNumber):
            oddIdx += 2

    return nums



def swap(i, j, nums):
    nums[i], nums[j] = nums[j], nums[i]


def isEven(num):
    return num % 2 == 0

def isOdd(num):
    return num % 2 != 0
