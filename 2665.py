import sys
from _collections import deque


def main():
    global N, board
    N = int(sys.stdin.readline())
    board = []
    for i in range(N):
        board.append(list(sys.stdin.readline()[:N]))
    print(bfs([0, 0]))



def bfs(pos):
    global N, board
    change = [[2501 for j in range(N)] for i in range(N)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    y, x = pos[0], pos[1]
    change[y][x] = 0
    q.append([y, x, 0])
    while len(q) > 0:
        y, x, cnt = q[0][0], q[0][1], q[0][2]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] == '1': #흰 방으로 갈 때
                    if cnt < change[ny][nx]:
                        change[ny][nx] = cnt
                        q.append([ny, nx, cnt])
                else: #검은방으로 갈 때
                    if cnt + 1 < change[ny][nx]:
                        change[ny][nx] = cnt + 1
                        q.append([ny, nx, cnt + 1])
        q.popleft()
    return change[N - 1][N - 1]


if __name__ == '__main__':
    main()
