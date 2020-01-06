def knight_move(row, col):
    """knight_move (row, col) - returns all possible movements for the
    knight in chess based on the parameters of its current row and column"""

    # Deltas and Column Names
    columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
    possible_moves = [(2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2)]
    new_pos = []
    new_pos_l = []
    col = columns.index(col) + 1

    # Applying deltas to current position
    for r, c in possible_moves:
        moves = row + r, col + c
        new_pos.append(moves)

    # Filtering only valid positions in the board
    new_pos = [(row, col) for row, col in new_pos if 0 < row <= 8 and 0 < col <= 8]

    # Changing integer back to column letter
    for row, col in new_pos:
        letters = row, columns[col - 1]
        new_pos_l.append(letters)
    return new_pos_l


print(knight_move(7, "D"))
