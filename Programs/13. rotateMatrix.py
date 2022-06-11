def rotateMatrix(matrix):

    startRow = startCol = 0
    endRow = endCol = len(matrix) - 1

    while startRow <= endRow and startCol <= endCol:

        n = endCol - startCol

        for currentPosition in range(n):
            temp = matrix[endRow][endCol - currentPosition]

            matrix[endRow][endCol - currentPosition] = matrix[startRow + currentPosition][endCol]

            matrix[startRow + currentPosition][endCol] = matrix[startRow][startCol + currentPosition]

            matrix[startRow][startCol + currentPosition] = matrix[endRow - currentPosition][startCol]

            matrix[endRow - currentPosition][startCol] = temp


        startRow += 1
        startCol += 1
        endCol -= 1
        endRow -= 1

    return matrix
        
