

def sumAndSearch(array, target):


    isTargetFound = False
    totalSum = 0

    for value in array:

        if target == value:
            isTargetFound = True

        totalSum += value

    return [totalSum, isTargetFound]
