import sys
from collections import deque


def main():
    global N, board, visit, ans
    N = int(sys.stdin.readline())
    board, doors, visit = [], [], []
    ans = 2501
    for i in range(N):
        board.append(list(sys.stdin.readline()[:N]))
        for j in range(N):
            if board[i][j] == '#':
                doors.append([i, j])
    visit = [[[2502 for k in range(4)] for j in range(N)] for i in range(N)]
    bfs(doors[0], doors[1])
    print(ans)


def bfs(start, end):
    global N, board, visit, ans
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    sy, sx, ey, ex = start[0], start[1], end[0], end[1]
    q = deque()
    for i in range(4):
        ny, nx = sy + dy[i], sx + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if board[ny][nx] != '*':
                q.append([sy, sx, i, 0])
                visit[sy][sx][i] = 0
    while len(q) > 0:
        y, x, dir, cnt = q[0][0], q[0][1], q[0][2], q[0][3]
        ny, nx = y + dy[dir], x + dx[dir]
        if board[y][x] == '.': #직선
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != '*' and visit[ny][nx][dir] >= cnt:
                q.append([ny, nx, dir, cnt])
                visit[ny][nx][dir] = cnt
        elif board[y][x] == '!': # 거울 설치가능
            v1 = [dy[dir], dx[dir]]
            for i in range(4):
                v2 = [dy[i], dx[i]]
                ny, nx, ndir = y + dy[i], x + dx[i], i
                if v1[0] * v2[0] + v1[1] * v2[1] == 0: # 90도로 꺾임
                    if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != '*' and visit[ny][nx][ndir] >= cnt + 1:
                        q.append([ny, nx, ndir, cnt + 1])
                        visit[ny][nx][ndir] = cnt + 1
                if v1[0] * v2[0] + v1[1] * v2[1] == 1: # 직선으로 진행
                    if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != '*' and visit[ny][nx][ndir] >= cnt:
                        q.append([ny, nx, dir, cnt])
                        visit[ny][nx][dir] = cnt
        elif board[y][x] == '#':
            if y == ey and x == ex:
                if cnt <= ans:
                    ans = cnt
            else: # 시작점일떄
                if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != '*' and visit[ny][nx][dir] >= cnt:
                    q.append([ny, nx, dir, cnt])
                    visit[ny][nx][dir] = cnt
        q.popleft()


if __name__ == '__main__':
    main()
