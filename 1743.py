import sys
from collections import deque


def main():
    N, M, K = map(int, sys.stdin.readline().split())
    board = [[0 for j in range(M)] for i in range(N)]
    visit = [[0 for j in range(M)] for i in range(N)]
    for _ in range(K):
        r, c = map(int, sys.stdin.readline().split())
        board[r - 1][c - 1] = 1
    ans = 0
    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0 and board[i][j] == 1:
                ans = max(ans, bfs(i, j, board, visit, N, M))
    print(ans)


def bfs(sY, sX, board, visit, N, M):
    cnt = 1
    visit[sY][sX] = 1
    q = deque()
    q.append([sY, sX])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and visit[ny][nx] == 0 and board[ny][nx] == 1:
                cnt += 1
                visit[ny][nx] = 1
                q.append([ny, nx])
    return cnt


if __name__ == "__main__":
    main()
