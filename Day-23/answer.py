def dfs(i, j, visited, board):
    if (
        i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or
        board[i][j] != 'O' or visited[i][j]
    ):
        return
    visited[i][j] = True

    dfs(i + 1, j, visited, board)
    dfs(i - 1, j, visited, board)
    dfs(i, j + 1, visited, board)
    dfs(i, j - 1, visited, board)

def solve(board):
    n = len(board)
    m = len(board[0])

    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        dfs(i, 0, visited, board)
        dfs(i, m - 1, visited, board)
    for j in range(m):
        dfs(0, j, visited, board)
        dfs(n - 1, j, visited, board)

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'O' and not visited[i][j]:
                board[i][j] = 'X'

board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]

solve(board)

for row in board:
    print(row)
