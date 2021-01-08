import sys
from collections import deque


def main():
    global n, m, board, wall, visit, dy, dx
    n, m = map(int, sys.stdin.readline().split())
    board = []
    zone = []
    dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
    wall = [[[0, 0, 0, 0] for j in range(n)] for i in range(m)]
    visit = [[-1 for j in range(n)] for i in range(m)]
    ans3 = 0
    for i in range(m):
        board.append(list(map(int, sys.stdin.readline().split())))
    cnt = 0 # 몇번 공간인지 확인
    for i in range(m):
        for j in range(n):
            num = board[i][j]
            getwall(num, [i, j])
    for i in range(m):
        for j in range(n):
            if visit[i][j] == -1:
                zone.append(bfs([i, j], cnt))
                cnt += 1 # n번째 공간에서 n + 1공간으로 넘어감
    for i in range(m):
        for j in range(n):
            for k in range(4):
                ni, nj = i + dy[k], j + dx[k]
                if 0 <= ni < m and 0 <= nj < n:
                    if visit[i][j] != visit[ni][nj]:
                        aIdx, bIdx = visit[i][j], visit[ni][nj]
                        tmp = zone[aIdx] + zone[bIdx]
                        if ans3 <= tmp:
                            ans3 = tmp
    print(len(zone))
    print(max(zone))
    print(ans3)


def bfs(pos, cnt):
    global n, m, board, wall, visit, dy, dx
    q = deque()
    q.append(pos)
    visit[pos[0]][pos[1]] = cnt
    area = 1 # 넓이 셈
    while len(q) > 0:
        y, x = q[0][0], q[0][1]
        wallchk = wall[y][x]
        for i in range(4):
            if wallchk[i] == 0:
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < m and 0 <= nx < n and visit[ny][nx] == -1:
                    visit[ny][nx] = cnt
                    area += 1
                    q.append([ny, nx])
        q.popleft()
    return area


def getwall(num, pos):
    global board, wall
    y, x = pos[0], pos[1]
    if num >= 8:
        num -= 8
        wall[y][x][3] = 1
    if num >= 4:
        num -= 4
        wall[y][x][2] = 1
    if num >= 2:
        num -= 2
        wall[y][x][1] = 1
    if num >= 1:
        num -= 1
        wall[y][x][0] = 1


if __name__ == '__main__':
    main()
