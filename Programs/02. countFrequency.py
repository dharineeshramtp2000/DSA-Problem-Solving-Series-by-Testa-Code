def countFrequencyofTarget(array, target):

    counter = 0

    for value in array:
        if value == target:
            counter += 1

    return counter


def countAllFrequency(array):
    hashTable = {}

    for value in array:
        if value not in hashTable:
            hashTable[value] = 0

        hashTable[value] += 1

    return hashTable
