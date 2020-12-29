import sys
from collections import deque


def main():
    global N, M, P, S, board, visit, playerQue, area, dy, dx, endChk
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    N, M, P = map(int, sys.stdin.readline().split())
    S = list(map(int, sys.stdin.readline().split()))
    board = []
    playerQue = [deque() for i in range(P)]
    visit = [[0 for j in range(M)] for i in range(N)]
    area = [0 for i in range(P)]
    endChk = [0 for i in range(P)]
    for i in range(N):
        board.append(list(map(str, sys.stdin.readline()[:M])))
    for i in range(N):
        for j in range(M):
            if board[i][j] != '#' and board[i][j] != '.':
                board[i][j] = int(board[i][j])
                pIdx = board[i][j] - 1
                playerQue[pIdx].append([i, j, 0])
                area[pIdx] += 1
                visit[i][j] = 1
    while 1:
        for pIdx in range(P):
            bfs(pIdx)
        if sum(endChk) == P:
            break
    for i in range(P):
        print(area[i], end=' ')


def bfs(pIdx):
    global N, M, P, S, board, visit, playerQue, area, dy, dx, endChk
    q = playerQue[pIdx]
    if len(q) == 0:
        return
    std = q[0][2]
    maxDis = S[pIdx]
    nxtQ = deque()
    while len(q) > 0:
        y, x = q[0][0], q[0][1]
        dis = q[0][2]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and visit[ny][nx] == 0 and board[ny][nx] == '.':
                if dis + 1 - std <= maxDis:
                    board[ny][nx] = pIdx + 1
                    visit[ny][nx] = 1
                    q.append([ny, nx, dis + 1])
                    area[pIdx] += 1
        if dis - std == maxDis:
            nxtQ.append(q.popleft())
        else:
            q.popleft()
    playerQue[pIdx] = nxtQ
    if len(nxtQ) == 0:
        endChk[pIdx] = 1


if __name__ == '__main__':
    main()
