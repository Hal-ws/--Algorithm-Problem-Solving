import sys

board = []
length = []
for i in range(5):
    t = sys.stdin.readline()
    length.append(len(t))
    board.append(t[:len(t) - 1])

ans = ''
for j in range(max(length)):
    for i in range(5):
        if len(board[i]) < j + 1:
            i += 1
        else:
            ans += board[i][j]
print(ans)
