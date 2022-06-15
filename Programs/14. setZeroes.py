def setZeroes(matrix):

    isZeroInFirstCol = False

    m = len(matrix)
    n = len(matrix[0])

    for rowIdx in range(m):

        if matrix[rowIdx][0] == 0:
            isZeroInFirstCol = True

        for colIdx in range(1, n):
            if matrix[rowIdx][colIdx] == 0:

                matrix[rowIdx][0] = matrix[0][colIdx] = 0

    for rowIdx in range(m - 1, -1, -1):

        for colIdx in range(n - 1, 0, -1):
            if matrix[rowIdx][0] == 0 or matrix[0][colIdx] == 0:
                matrix[rowIdx][colIdx] = 0

        if isZeroInFirstCol:
            matrix[rowIdx][0] = 0

    return matrix
