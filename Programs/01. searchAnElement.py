def findTargetValue(array, target):

    for idx in range(len(array)):
        value = array[idx]

        if value == target:
            return True

    return False
    
    
