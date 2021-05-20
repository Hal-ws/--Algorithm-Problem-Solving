import sys
from collections import deque


def main():
    global N, M, board
    N, M = map(int, sys.stdin.readline().split())
    board = [[0 for j in range(M + 2)]]
    maxH, answer = 0, 0
    for i in range(N):
        tmp = list(map(int, sys.stdin.readline().split()))
        tmp = [0] + tmp + [0]
        board.append(tmp)
        if maxH <= max(tmp):
            maxH = max(tmp)
    board.append([0 for j in range(M + 2)])

    for i in range(N + 2):
        print(board[i])
    for stdH in range(maxH + 1):
        answer += bfs(stdH)
    print(answer)


def bfs(stdH):
    global N, M, board
    cnt = 0
    q = deque()
    visit = [[0 for j in range(M + 2)] for i in range(N + 2)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(N + 2):
        for j in range(M + 2):
            if board[i][j] > stdH:
                visit[i][j] = 1
    q.append([0, 0])
    visit[0][0] = 1
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N + 2 and 0 <= nx < M + 2 and visit[ny][nx] == 0:
                visit[ny][nx] = 1
                q.append([ny, nx])
    for i in range(N + 2):
        for j in range(M + 2):
            if visit[i][j] == 0:
                cnt += 1
    return cnt


if __name__ == '__main__':
    main()
