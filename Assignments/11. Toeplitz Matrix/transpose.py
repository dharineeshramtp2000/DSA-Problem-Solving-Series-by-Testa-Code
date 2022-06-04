def transpose(matrix):
    rowSize = len(matrix)
    colSize = len(matrix[0])

    result = [[None for _ in range(rowSize)] for _ in range(colSize)]

    for row in range(rowSize):
        for col in range(colSize):

            result[col][row] = matrix[row][col]

    return result
