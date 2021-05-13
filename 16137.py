import sys
from collections import deque


def main():
    global board, dy, dx, N
    N, M = map(int, sys.stdin.readline().split())
    board = []
    answer = 10000000000
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0: # 빈 공간 발견
                board[i][j] = M # 오작교 설치
                tmpResult = bfs()
                board[i][j] = 0
                if tmpResult < answer:
                    answer = tmpResult
    print(answer)


def bfs():
    global board, dy, dx, N
    visit = [[-1 for j in range(N)] for i in range(N)] # 미방문을 -1로 표시
    q = deque()
    visit[0][0] = 0
    q.append([0, 0, 0, 1])# 행, 열, 방문시간, 평지인지(1), 오작교 위인지(0)
    while len(q) > 0:
        tmp = q.popleft()
        y, x, t, flag = tmp[0], tmp[1], tmp[2], tmp[3]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if flag: #현재 평지. 오작교로 이동가능
                    if board[ny][nx] == 1: # 평지로 이동
                        if visit[ny][nx] == -1 or t + 1 < visit[ny][nx]:
                            q.append([ny, nx, t + 1, 1])
                            visit[ny][nx] = t + 1
                    if board[ny][nx] > 1: # 오작교로 이동
                        cycle = board[ny][nx]
                        nt = ((t // cycle) + 1) * cycle
                        if visit[ny][nx] == -1 or nt < visit[ny][nx]:
                            q.append([ny, nx, nt, 0])
                            visit[ny][nx] = nt
                else: #현재 오작교. 평지로만 이동가능
                    if board[ny][nx] == 1:
                        if visit[ny][nx] == -1 or t + 1 < visit[ny][nx]:
                            q.append([ny, nx, t + 1, 1])
                            visit[ny][nx] = t + 1
    if visit[N - 1][N - 1] != -1:
        return visit[N - 1][N - 1]
    return 10000000000


if __name__ == '__main__':
    main()
