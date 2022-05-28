def canThreePartsEqualSum(arr):

    #Entire Sum of Array
    total = sum(arr)

    #if totalSum is not divisible by 3 then we directly return False
    if(total % 3 != 0):
        return False


    partSum = total / 3
    currentSum = 0
    parts = 0
    for num in arr:
        currentSum += num
        if(currentSum == partSum):
            currentSum = 0
            parts += 1

    # Handling the case when arr = [0,0,0,0,0]
    return parts >= 3
