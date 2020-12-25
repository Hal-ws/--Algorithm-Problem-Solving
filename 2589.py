import sys
from collections import deque


def main():
    global N, M, distance, board
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(sys.stdin.readline()[:M]))
    distance = [[0 for j in range(M)] for i in range(N)]
    maxDis = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == "L":
                tmp = bfs([i, j])
                if maxDis <= tmp:
                    maxDis = tmp
    print(maxDis)


def bfs(start):
    global N, M, board
    visit = [[0 for j in range(M)] for i in range(N)]
    q = deque()
    q.append(start + [0])
    visit[q[0][0]][q[0][1]] = 1
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    answer = 0
    while len(q) > 0:
        for i in range(4):
            ny, nx = q[0][0] + dy[i], q[0][1] + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if visit[ny][nx] == 0 and board[ny][nx] == "L":
                    visit[ny][nx] = 1
                    q.append([ny, nx, q[0][2] + 1])
                    answer = q[0][2] + 1
        q.popleft()
    return answer


if __name__ == '__main__':
    main()
