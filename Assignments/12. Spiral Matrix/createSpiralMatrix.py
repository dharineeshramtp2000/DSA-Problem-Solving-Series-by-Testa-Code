def createSpiralMatrix(n):
    counter = 1

    matrix = [[None for _ in range(n)] for _ in range(n)]

    startRow = 0
    startCol = 0
    endRow = n -1
    endCol = n - 1


    while startRow <= endRow and startCol <= endCol:

        for idx in range(startRow, endCol + 1):
            matrix[startRow][idx] = counter
            counter += 1

        for idx in range(startRow + 1, endRow + 1):
            matrix[idx][endCol] = counter
            counter += 1

        for idx in range(endCol - 1, startCol - 1, -1):
            if startRow == endRow:
                break
            matrix[endCol][idx] = counter
            counter += 1


        for idx in range(endRow -1, startRow, -1):
            if startCol == endCol:
                break

            matrix[idx][startCol] = counter
            counter += 1

        startRow += 1
        endRow -= 1

        startCol += 1
        endCol -= 1

    return matrix
