from collections import deque
import sys


def main():
    global W, H, board, visit
    W, H = map(int, sys.stdin.readline().split())
    visit = [[10001 for j in range(W)] for i in range(H)]
    board, points = [], []
    for i in range(H):
        board.append(list(map(str, sys.stdin.readline()[:W])))
    for i in range(H):
        for j in range(W):
            if board[i][j] == "C":
                points.append([i, j])
    bfs(points[0], points[1])
    print(visit[points[1][0]][points[1][1]])


def bfs(start, end):
    global W, H, board, visit
    q = deque()
    q.append([start[0], start[1], -1, 0]) #y, x, 방향, 방향전환 cnt
    visit[q[0][0]][q[0][1]] = 0
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(4):
        y, x, dir, cnt = q[0][0], q[0][1], q[0][2], q[0][3]
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < H and 0 <= nx < W and board[ny][nx] == '.':
            visit[ny][nx] = 0
            q.append([ny, nx, i, 0])
    q.popleft()
    while len(q) > 0:
        y, x, dir, cnt = q[0][0], q[0][1], q[0][2], q[0][3]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < H and 0 <= nx < W and board[ny][nx] != '*':
                if i == dir: # 같은 방향으로 진행함
                    if cnt <= visit[ny][nx]:
                        visit[ny][nx] = cnt
                        q.append([ny, nx, i, cnt])
                else:
                    if cnt + 1 <= visit[ny][nx]:
                        visit[ny][nx] = cnt + 1
                        q.append([ny, nx, i, cnt + 1])
        q.popleft()


if __name__ == '__main__':
    main()
