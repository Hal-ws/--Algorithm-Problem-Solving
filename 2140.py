import sys

def removemine(i, j, board):
    if type(board[i - 1][j - 1]) == int:
        board[i - 1][j - 1] -= 1
    if type(board[i - 1][j]) == int:
        board[i - 1][j] -= 1
    if type(board[i - 1][j + 1]) == int:
        board[i - 1][j + 1] -= 1
    if type(board[i][j + 1]) == int:
        board[i][j + 1] -= 1
    if type(board[i + 1][j + 1]) == int:
        board[i + 1][j + 1] -= 1
    if type(board[i + 1][j]) == int:
        board[i + 1][j] -= 1
    if type(board[i + 1][j - 1]) == int:
        board[i + 1][j - 1] -= 1
    if type(board[i][j - 1]) == int:
        board[i][j - 1] -= 1
    board[i][j] = '.'
N = int(sys.stdin.readline())
board = [0] * N
for i in range(N):
    board[i] = list(sys.stdin.readline())[:N]
for i in range(N):
    for j in range(N):
        if board[i][j] != '#':
            board[i][j] = int(board[i][j])
if board[0][0] == 1:
    removemine(1, 1, board)
for i in range(5):
    print(board[i])
if board[0][N - 1] == 1:
    removemine(1, N - 2, board)
for i in range(5):
    print(board[i])
if board[N - 1][0] == 1:
    removemine(N - 2, 1, board)
for i in range(5):
    print(board[i])
if board[N - 1][N - 1] == 1:
    removemine(N - 2, N - 2, board)
for i in range(5):
    print(board[i])
