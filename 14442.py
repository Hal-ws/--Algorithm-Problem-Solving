import sys
from collections import deque


def main():
    global N, M, K, board
    N, M, K = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(sys.stdin.readline()[:M])
    print(bfs([0, 0]))


def bfs(pos):
    global N, M, K, board
    visit = [[[0] * (K + 1) for j in range(M)] for i in range(N)] # 지나간 칸, 이동거리
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    y, x = pos[0], pos[1]
    q.append([y, x, 1, 0])
    visit[0][0][0] = 1
    while len(q) > 0:
        y, x, dis, crash = q[0][0], q[0][1], q[0][2], q[0][3] #좌표, 이동거리, 부순것
        if y == N - 1 and x == M - 1:
            return dis
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx] == '1' and crash < K: # 벽일때
                    if visit[ny][nx][crash + 1] == 0 or dis + 1 < visit[ny][nx][crash + 1]:
                        visit[ny][nx][crash + 1] = dis + 1
                        q.append([ny, nx, dis + 1, crash + 1])
                if board[ny][nx] == '0':
                    if visit[ny][nx][crash] == 0 or dis + 1 < visit[ny][nx][crash]:
                        visit[ny][nx][crash] = dis + 1
                        q.append([ny, nx, dis + 1, crash])
        q.popleft()
    return -1


if __name__ == '__main__':
    main()
