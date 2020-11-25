import sys
from collections import deque


def main():
    N, M, R = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    lUp, rDown = [0, 0], [N - 1, M - 1]
    while 1:
        rotation(board, lUp, rDown, R)
        lUp[0] += 1
        lUp[1] += 1
        rDown[0] -= 1
        rDown[1] -= 1
        if lUp[0] > rDown[0] or lUp[1] > rDown[1]:
            break
    for i in range(N):
        for j in range(M):
            print(board[i][j], end=' ')
        print()


def rotation(board, lUp, rDown, R):
    i, j = lUp[0], lUp[1]
    q = deque()
    while 1:
        q.append(board[i][j])
        if i == rDown[0]:
            break
        i += 1
    j += 1
    while 1:
        q.append(board[i][j])
        if j == rDown[1]:
            break
        j += 1
    i -= 1
    while 1:
        q.append(board[i][j])
        if i == lUp[0]:
            break
        i -= 1
    while 1:
        j -= 1
        if j == lUp[1]:
            break
        q.append(board[i][j])
    q.rotate(R)
    while 1:
        board[i][j] = q.popleft()
        if i == rDown[0]:
            break
        i += 1
    j += 1
    while 1:
        board[i][j] = q.popleft()
        if j == rDown[1]:
            break
        j += 1
    i -= 1
    while 1:
        board[i][j] = q.popleft()
        if i == lUp[0]:
            break
        i -= 1
    j -= 1
    while 1:
        if j == lUp[1]:
            break
        board[i][j] = q.popleft()
        j -= 1


if __name__ == "__main__":
    main()
