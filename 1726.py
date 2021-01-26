import sys
from collections import deque


def main():
    global M, N, board
    M, N = map(int, sys.stdin.readline().split())
    board = []
    for i in range(M):
        board.append(list(map(int, sys.stdin.readline().split())))
    start = list(map(int, sys.stdin.readline().split()))
    end = list(map(int, sys.stdin.readline().split()))
    start[0], start[1], start[2] = start[0] - 1, start[1] - 1, start[2] - 1
    end[0], end[1], end[2] = end[0] - 1, end[1] - 1, end[2] - 1
    print(bfs(start, end))


def bfs(start, end):
    global M, N, board
    visit = [[[0 for k in range(4)] for j in range(N)] for i in range(M)]
    dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
    q = deque()
    q.append([start[0], start[1], start[2], 0])
    visit[start[0]][start[1]][start[2]] = 1
    while len(q) > 0:
        y, x, d, cnt = q[0][0], q[0][1], q[0][2], q[0][3]
        if y == end[0] and x == end[1] and d == end[2]:
            return cnt
        for k in range(1, 4): #k 만큼 움직임
            if d == 0 or d == 1:
                ny, nx = y + dy[d], x + dx[d] * k
                if 0 <= ny < M and 0 <= nx < N and visit[ny][nx][d] == 0:
                    if board[ny][nx] == 1:
                        break
                    else:
                        q.append([ny, nx, d, cnt + 1])
                        visit[ny][nx][d] = 1
            if d == 2 or d == 3:
                ny, nx = y + dy[d] * k, x + dx[d]
                if 0 <= ny < M and 0 <= nx < N and visit[ny][nx][d] == 0:
                    if board[ny][nx] == 1:
                        break
                    else:
                        q.append([ny, nx, d, cnt + 1])
                        visit[ny][nx][d] = 1
        if d == 0 or d == 1:
            if visit[y][x][2] == 0:
                q.append([y, x, 2, cnt + 1])
                visit[y][x][2] = 1
            if visit[y][x][3] == 0:
                q.append([y, x, 3, cnt + 1])
                visit[y][x][3] = 1
        if d == 2 or d == 3:
            if visit[y][x][0] == 0:
                q.append([y, x, 0, cnt + 1])
                visit[y][x][0] = 1
            if visit[y][x][1] == 0:
                q.append([y, x, 1, cnt + 1])
                visit[y][x][1] = 1
        q.popleft()


if __name__ == '__main__':
    main()
