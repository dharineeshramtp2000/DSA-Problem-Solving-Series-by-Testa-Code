def toeplitzMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])


    for rowIdx in range(m):
        for colIdx in range(n):

            if rowIdx > 0 and colIdx > 0 and matrix[rowIdx][colIdx] != matrix[rowIdx - 1][colIdx - 1]:
                False
    return True

    
