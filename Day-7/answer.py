def is_valid(board, row, col, num):
    """Checks if placing 'num' at (row, col) is valid."""
    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    """Solves the Sudoku puzzle using backtracking."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def print_board(board):
    """Prints the solved Sudoku grid."""
    for row in board:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    board = [
        [0, 4, 0, 0, 0, 0, 1, 7, 9],
        [0, 0, 2, 0, 0, 8, 0, 5, 4],
        [0, 0, 6, 0, 0, 5, 0, 0, 8],
        [0, 8, 0, 0, 7, 0, 9, 1, 0],
        [0, 5, 0, 0, 9, 0, 0, 3, 0],
        [0, 1, 9, 0, 6, 0, 0, 4, 0],
        [3, 0, 0, 4, 0, 0, 7, 0, 0],
        [5, 7, 0, 1, 0, 0, 2, 0, 0],
        [9, 2, 8, 0, 0, 0, 0, 6, 0]
    ]

    if solve_sudoku(board):
        print_board(board)
    else:
        print("-1")