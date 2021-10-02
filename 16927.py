import sys
from collections import deque


def main():
    N, M, R = map(int, sys.stdin.readline().split())
    board = []
    R = R % (2 * N + 2 * (M - 2))
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    board = trying(board, N, M, R)
    for i in range(N):
        for j in range(M):
            print(board[i][j], end=' ')
        print()


def trying(board, h, w, R):
    newBoard = [[0 for j in range(w)] for i in range(h)]
    sy, sx = 0, 0
    while 1:
        q = deque()
        y, x = sy, sx
        for i in range(y, h):
            if newBoard[i][x] != 0:
                break
            q.append(board[i][x])
            y = i
        for j in range(x + 1, w):
            if newBoard[y][j] != 0:
                break
            q.append(board[y][j])
            x = j
        for i in range(y - 1, sy - 1, -1):
            if newBoard[i][x] != 0:
                break
            q.append(board[i][x])
            y = i
        for j in range(x - 1, sx, -1):
            if newBoard[y][j] != 0:
                break
            q.append(board[y][j])
        for i in range(R):
            q.appendleft(q.pop())
        y, x = sy, sx
        for i in range(y, h):
            if newBoard[i][x] != 0:
                break
            newBoard[i][x] = q.popleft()
            y = i
        for j in range(x + 1, w):
            if newBoard[y][j] != 0:
                break
            newBoard[y][j] = q.popleft()
            x = j
        for i in range(y - 1, sy - 1, -1):
            if newBoard[i][x] != 0:
                break
            newBoard[i][x] = q.popleft()
            y = i
        for j in range(x - 1, sx, -1):
            if newBoard[y][j] != 0:
                break
            newBoard[y][j] = q.popleft()
        sy, sx = sy + 1, sx + 1
        if newBoard[sy][sx] != 0:
            break
    return newBoard


if __name__ == "__main__":
    main()
