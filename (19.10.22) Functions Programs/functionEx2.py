def knightMove(row,col):
    #Takes in knight's current position and returns possible moves
    
    #Deltas and Column Names
    columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
    possibleMoves = [(2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2)]
    
    newPos = []
    newPosL = []
    col = columns.index(col)
    
    #Applying deltas to current position
    for r, c in possibleMoves:
        moves = row+r, col+c
        
        
        newPos.append(moves)
    col = columns[col]
    
    #Filtering only valid positions in the board
    newPos = [(row,col) for row, col in newPos if row > 0 and col > 0 and row <= 8 and col <= 8]
    
    #Changing interger back to column letter
    for row, col in newPos:
        letters = row, columns[col]
        
        newPosL.append(letters)
    return newPosL

print(knightMove(8,"A"))