def numRookCaptures(board):
    rookRowIdx, rookColIdx = getRookLocation(board)

    n = len(board)

    availableCaptures = 0

    #Traverse Top. Row Index changes

    for rowIdx in range(rookRowIdx - 1, -1, -1):

        currentSquare = board[rowIdx][rookColIdx]
        if currentSquare == "p":
            availableCaptures += 1
            break

        if currentSquare == "B":
            break

    #Traverse Bottom. Row Index changes

    for rowIdx in range(rookRowIdx + 1, n):

        currentSquare = board[rowIdx][rookColIdx]
        if currentSquare == "p":
            availableCaptures += 1
            break

        if currentSquare == "B":
            break


    #Traverse Left. Column Index changes

    for colIdx in range(rookColIdx - 1, -1, -1):

        currentSquare = board[rookRowIdx][colIdx]
        if currentSquare == "p":
            availableCaptures += 1
            break

        if currentSquare == "B":
            break

    #Traverse Right. Column Index changes

    for colIdx in range(rookColIdx + 1, n):

        currentSquare = board[rookRowIdx][colIdx]
        if currentSquare == "p":
            availableCaptures += 1
            break

        if currentSquare == "B":
            break


    return availableCaptures




def getRookLocation(board):

    for rowIdx in range(len(board)):

        for colIdx in range(len(board)):

            if board[rowIdx][colIdx] == "R":
                return [rowIdx, colIdx]
