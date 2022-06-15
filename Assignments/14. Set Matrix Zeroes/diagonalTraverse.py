def diagonalTraverse(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row = 0
    col = 0

    goDown = False
    result = []

    while (row >= 0 and row < m) and (col >= 0 and col < n):
        result.append(matrix[row][col])


        if goDown:
            if row != m - 1 and col != 0:
                row += 1
                col -= 1
                continue

            if row == m - 1:
                col += 1

            elif col == 0:
                row += 1
            goDown = False

        else:
            if row != 0 and col != n - 1:
                row -= 1
                col += 1
                continue

            if col == n -1:
                row += 1

            elif row == 0:
                col += 1

            goDown = True


    return result
