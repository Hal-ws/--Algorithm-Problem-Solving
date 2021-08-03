import sys
from collections import deque


def main():
    N, M = map(int, sys.stdin.readline().split())
    before, after = [], []
    for i in range(N):
        before.append(list(map(int, sys.stdin.readline().split())))
    for i in range(N):
        after.append(list(map(int, sys.stdin.readline().split())))
    cBoard = [[0 for j in range(M)] for i in range(N)]
    cIdx = 1
    for i in range(N):
        for j in range(M):
            if cBoard[i][j] == 0:
                coloring(before, cBoard, cIdx, i, j, N, M)
                cIdx += 1
    if chk(before, after, cBoard, N, M):
        print('YES')
    else:
        print('NO')
            

def chk(before, after, cBoard, N, M):
    return 0
                

def coloring(before, cBoard, cIdx, sy, sx, N, M):
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    visit = [[0 for j in range(M)] for i in range(N)]
    visit[sy][sx] = 1
    std = before[sy][sx]
    cBoard[sy][sx] = cIdx
    q.append([sy, sx])
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and visit[ny][nx] == 0 and before[ny][nx] == std:
                q.append([ny, nx])
                cBoard[ny][nx] = cIdx
                visit[ny][nx] = 1

    


if __name__ == '__main__':
    main()
