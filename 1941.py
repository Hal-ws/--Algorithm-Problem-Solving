import sys
from itertools import combinations
from collections import deque


def main():
    global board, dy, dx
    board = []
    pos = []
    ans = 0
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(5):
        board.append(list(sys.stdin.readline()[:5]))
    for i in range(5):
        for j in range(5):
            pos.append([i, j])
    cases = combinations(pos, 7)
    for case in cases:
        if getans(case):
            ans += 1
    print(ans)


def getans(case):
    global board
    sits = [[0 for j in range(5)] for i in range(5)]
    cnt = 0
    for pos in case:
        y, x = pos[0], pos[1]
        sits[y][x] = 1
    if bfs(sits, case[0][0], case[0][1]) == 0:
        return 0 # 흩어져 앉아있음
    for i in range(5):
        for j in range(5):
            if sits[i][j] == 1 and board[i][j] == "S":
                cnt += 1
    if cnt >= 4:
        return 1
    else:
        return 0


def bfs(sits, y, x):
    global dy, dx
    visit = [[0 for j in range(5)] for i in range(5)]
    q = deque()
    visit[y][x] = 1
    q.append([y, x])
    cnt = 1
    while len(q) > 0:
        y, x = q[0][0], q[0][1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5 and visit[ny][nx] == 0 and sits[ny][nx] == 1:
                visit[ny][nx] = 1
                q.append([ny, nx])
                cnt += 1
        q.popleft()
    if cnt == 7:
        return 1
    else:
        return 0


if __name__ == '__main__':
    main()
