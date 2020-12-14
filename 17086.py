import sys
from collections import deque


def main():
    N, M = map(int, sys.stdin.readline().split())
    board, sharks, sharksCnt = [], [], 0
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    disBoard = [[0 for j in range(M)] for i in range(N)]
    for i in range(sharksCnt):
        bfs(board, sharks[i], disBoard[i], N, M)
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                disBoard[i][j] = bfs(board, [i, j], N, M)
    maxDis = 0
    for i in range(N):
        for j in range(M):
            if maxDis <= disBoard[i][j]:
                maxDis = disBoard[i][j]
    print(maxDis)


def bfs(board, pos, N, M):
    y, x = pos[0], pos[1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    chk = [[0 for j in range(M)] for i in range(N)]
    q = deque()
    q.append([0, y, x])
    chk[y][x] = 1
    while len(q) > 0:
        y, x = q[0][1], q[0][2]
        dis = q[0][0]
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and chk[ny][nx] == 0:
                if board[ny][nx] == 0:#비어있고 방문안한 지점
                    chk[ny][nx] = 1
                    q.append([dis + 1, ny, nx])
                if board[ny][nx] == 1:# 상어 만남
                    return dis + 1
        q.popleft()


if __name__ == '__main__':
    main()
