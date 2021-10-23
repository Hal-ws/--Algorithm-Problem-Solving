import sys
from collections import deque
from itertools import combinations


def main():
    N, M = map(int, sys.stdin.readline().split())
    board = []
    viruses = []
    ans = 2501
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
        for j in range(N):
            if board[i][j] == 2:
                viruses.append([i, j])  # 바이러스의 좌표 저장
    cases = list(combinations(viruses, M))
    for case in cases:
        ans = min(ans, bfs(board, case, N))
    if ans == 2501:
        print(-1)
    else:
        print(ans)


def bfs(board, useVirus, N):
    q = deque()
    visit = [[-1 for j in range(N)] for i in range(N)]
    for pos in useVirus:
        y, x = pos[0], pos[1]
        q.append([y, x, 0])
        visit[y][x] = 0
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while len(q) > 0:
        tmp = q.popleft()
        y, x, t = tmp[0], tmp[1], tmp[2]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != 1 and visit[ny][nx] <= -1:  # 이동가능하고 방문 안한곳일때
                visit[ny][nx] = t + 1
                q.append([ny, nx, t + 1])
    result = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 and visit[i][j] == -1:
                return 2501
            if board[i][j] == 2:
                visit[i][j] = 0
            result = max(result, visit[i][j])
    return result


if __name__ == "__main__":
    main()
