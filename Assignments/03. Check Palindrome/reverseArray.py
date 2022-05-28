def reverseArray(array):

    i = 0
    j = len(array) - 1


    while i <= j:
        swap(i, j, array)
        i += 1
        j -= 1

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
