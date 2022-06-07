def spiralMatrix(matrix):
    startRow = 0
    startCol = 0
    endRow = len(matrix) - 1
    endCol = len(matrix[0]) - 1

    result = []

    while startRow <= endRow and startCol <= endCol:

        #Traverse to Right

        for colIdx in range(startCol, endCol + 1):
            result.append(matrix[startRow][colIdx])

        #Traverse to Bottom

        for rowIdx in range(startRow + 1, endRow + 1):
            result.append(matrix[rowIdx][endCol])

        #Traverse to Left

        if startRow != endRow:
            for colIdx in range(endCol - 1, startCol - 1, -1):
                result.append(matrix[endRow][colIdx])


        #Traverse to Top
        if startCol != endCol:
            for rowIdx in range(endRow - 1, startRow, -1):
                result.append(matrix[rowIdx][startCol])


        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result
