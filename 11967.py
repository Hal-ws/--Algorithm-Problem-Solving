import sys
from collections import deque


def main():
    N, M = map(int, sys.stdin.readline().split())
    visit = [[0 for j in range(N)] for i in range(N)]
    light = [[0 for j in range(N)] for i in range(N)]
    connect = [[[] for j in range(N)] for i in range(N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visit[0][0] = 1
    light[0][0] = 1
    answer = 0
    q = deque()
    q.append([0, 0])
    for i in range(M):
        x, y, a, b = map(int, sys.stdin.readline().split())
        x, y, a, b = x - 1, y - 1, a - 1, b - 1
        connect[y][x].append([b, a])
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        for nxt in connect[y][x]:
            y1, x1 = nxt[0], nxt[1]
            light[y1][x1] = 1
            if visit[y1][x1] == 0:
                flag = 0
                for i in range(4):
                    ny, nx = y1 + dy[i], x1 + dx[i]
                    if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == 1:
                        flag = 1
                        break
                if flag:
                    visit[y1][x1] = 1
                    q.append([y1, x1])
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and light[ny][nx] == 1 and visit[ny][nx] == 0:
                q.append([ny, nx])
                visit[ny][nx] = 1
    for i in range(N):
        for j in range(N):
            answer += light[i][j]
    print(answer)


if __name__ == '__main__':
    main()
