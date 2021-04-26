from _collections import deque


def solution(maps):
    N = len(maps)
    M = len(maps[0])
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    visit = [[-1 for j in range(M)] for i in range(N)]
    q.append([0, 0, 1])
    visit[0][0] = 1
    while len(q) > 0:
        tmp = q.popleft()
        y, x, cnt = tmp[0], tmp[1], tmp[2]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and visit[ny][nx] == -1 and maps[ny][nx] == 1:
                q.append([ny, nx, cnt + 1])
                visit[ny][nx] = cnt + 1
    return visit[N - 1][M - 1]
