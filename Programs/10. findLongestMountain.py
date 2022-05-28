def longestMountain(array):
    idx = 1

    maxLength = 0

    while idx < len(array):

        leftSize = 0
        i = idx - 1

        while i >= 0 and array[i] < array[i + 1]:
            leftSize += 1
            i -= 1

        rightSize = 0
        j = idx + 1

        while j < len(array) and array[j] < array[j - 1]:
            rightSize += 1
            j += 1

        length = leftSize + rightSize + 1

        if length < 3:
            idx += 1
            continue

        maxLength = max(maxLength, length)
        idx += 1

    return maxLength
