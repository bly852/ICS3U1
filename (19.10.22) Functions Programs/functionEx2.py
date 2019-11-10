def knightMove(row,col):
    #Takes the row and column of the knight and returns a tuple of all possible moves
    columns = ("A", "B", "C", "D", "E", "F", "G", "H")
    rows = range(1,9)
    moves = ((2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2))
    
    pos = (row, col.capitalize())