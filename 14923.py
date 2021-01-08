import sys
from collections import deque
from itertools import combinations


def main():
    global N, M, board, dis, dy, dx, cdir
    N, M = map(int, sys.stdin.readline().split())
    hx, hy = map(int, sys.stdin.readline().split())
    ex, ey = map(int, sys.stdin.readline().split())
    board = []
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    ans = -1
    cdir = list(combinations([[-1, 0], [1, 0], [0, -1], [0, 1]], 2))
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    dis = [[[-1, -1] for j in range(M)] for i in range(N)]
    bfs([hx - 1, hy - 1], 0)
    bfs([ex - 1, ey - 1], 1)
    dis[hx - 1][hy - 1][0] = 0
    dis[ex - 1][ey - 1][1] = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1: # 벽일때 제거 시도
                tmp = connect([i, j])
                if tmp != None:
                    if ans == -1:
                        ans = tmp
                    else:
                        if tmp <= ans:
                            ans = tmp
    if dis[hx - 1][hy - 1][1] != -1: #연결은 됨
        if ans == -1: #벽 부숴서 연결한게 없음
            print(dis[hx - 1][hy - 1][1])
        else:
            print(min(ans, dis[hx - 1][hy - 1][1]))
    else:
        print(ans)


def connect(pos):
    global N, M, board, cdir, dis
    y, x = pos[0], pos[1]
    result = 999999999999
    for i in range(6):
        d0, d1 = cdir[i][0], cdir[i][1]
        y0, x0, y1, x1 = y + d0[0], x + d0[1], y + d1[0], x + d1[1]
        dis1, dis2 = 999999999999, 999999999999
        if 0 <= y0 < N and 0 <= x0 < M and 0 <= y1 < N and 0 <= x1 < M:
            if dis[y0][x0][0] != -1 and dis[y1][x1][1] != -1:
                dis1 = dis[y0][x0][0] + dis[y1][x1][1]
            if dis[y0][x0][1] != -1 and dis[y1][x1][0] != -1:
                dis2 = dis[y0][x0][1] + dis[y1][x1][0]
        tmp = min(dis1, dis2) + 2
        if tmp < result:
            result = tmp
    if result == 999999999999:
        return None
    else:
        return result


def bfs(pos, idx):
    global N, M, board, dis, dy, dx
    visit = [[0 for j in range(M)] for i in range(N)]
    y, x = pos[0], pos[1]
    q = deque()
    q.append([y, x, 0])
    visit[y][x] = 1
    while len(q) > 0:
        y, x, d = q[0][0], q[0][1], q[0][2]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and visit[ny][nx] == 0 and board[ny][nx] == 0:
                visit[ny][nx] = 1
                q.append([ny, nx, d + 1])
                dis[ny][nx][idx] = d + 1
        q.popleft()


if __name__ == '__main__':
    main()
