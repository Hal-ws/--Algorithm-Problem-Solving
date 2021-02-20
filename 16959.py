import sys
from _collections import deque


def main():
    global N, board, ans
    N = int(sys.stdin.readline())
    board = []
    ans = None
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    bfs()
    print(ans)


def bfs():
    global N, board, ans
    visit = [[[[0 for h in range(3)] for n in range(N * N + 1)] for j in range(N)] for i in range(N)]
    q = deque()
    kdy, kdx = [-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]
    bdy, bdx = [-1, -1, 1, 1], [-1, 1, -1, 1]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                y, x = i, j
                break
    for i in range(3):
        q.append([y, x, 0, 2, i]) # y, x좌표, 움직인 횟수, 다음 숫자, 말의 종류(0, 1, 2: knight, bishop, rook)
        visit[y][x][2][i] = 1
    while len(q) > 0:
        y, x, cnt, nxt, h = q[0][0], q[0][1], q[0][2], q[0][3], q[0][4]
        if nxt == N * N + 1: #끝에 다 도착
            if ans == None or cnt < ans:
                ans = cnt
            q.popleft()
            continue
        for i in range(3):
            if visit[y][x][nxt][i] == 0:
                visit[y][x][nxt][i] = 1
                q.append([y, x, cnt + 1, nxt, i])
        if h == 0: # knight
            for i in range(8):
                ny, nx = y + kdy[i], x + kdx[i]
                if 0 <= ny < N and 0 <= nx < N and visit[ny][nx][nxt][0] == 0:
                    visit[ny][nx][nxt][0] = 1
                    if board[ny][nx] == nxt:
                        q.append([ny, nx, cnt + 1, nxt + 1, 0])
                    else:
                        q.append([ny, nx, cnt + 1, nxt, 0])
        if h == 1:
            for i in range(4):
                d = 1
                while 1:
                    ny, nx = y + d * bdy[i], x + d * bdx[i]
                    if 0 <= ny < N and 0 <= nx < N:
                        if visit[ny][nx][nxt][1] == 0:
                            visit[ny][nx][nxt][1] = 1
                            if board[ny][nx] == nxt:
                                q.append([ny, nx, cnt + 1, nxt + 1, 1])
                            else:
                                q.append([ny, nx, cnt + 1, nxt, 1])
                    else:
                        break
                    d += 1
        if h == 2:
            for i in range(N):
                if visit[i][x][nxt][2] == 0:
                    visit[i][x][nxt][2] = 1
                    if board[i][x] == nxt:
                        q.append([i, x, cnt + 1, nxt + 1, 2])
                    else:
                        q.append([i, x, cnt + 1, nxt, 2])
            for j in range(N):
                if visit[y][j][nxt][2] == 0:
                    visit[y][j][nxt][2] = 1
                    if board[y][j] == nxt:
                        q.append([y, j, cnt + 1, nxt + 1, 2])
                    else:
                        q.append([y, j, cnt + 1, nxt, 2])
        q.popleft()

if __name__ == '__main__':
    main()
