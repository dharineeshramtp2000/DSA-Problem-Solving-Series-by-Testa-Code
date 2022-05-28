def moveTargetToEnd(array, target):
    i = 0
    j = len(array) - 1

    while i < j:
        if array[j] == target:
            j -= 1
            continue

        if array[i] != target:
            i += 1
            continue

        swap(i, j, array)

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
