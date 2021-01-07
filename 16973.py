import sys
from collections import deque


def main():
    global board, N, M, H, W
    board = []
    N, M = map(int, sys.stdin.readline().split())
    visit = [[0 for j in range(M)] for i in range(N)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    ans = -1
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    H, W, Sr, Sc, Fr, Fc = map(int, sys.stdin.readline().split())
    Sr, Sc, Fr, Fc = Sr - 1, Sc - 1, Fr - 1, Fc - 1
    visit[Sr][Sc] = 1
    q.append([Sr, Sc, 0])
    while len(q) > 0:
        y, x, cnt = q[0][0], q[0][1], q[0][2]
        if y == Fr and x == Fc:
            ans = cnt
            break
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if 0 <= ny + H - 1 < N and 0 <= nx + W - 1 < M and visit[ny][nx] == 0:
                    flag = 1
                    for j in range(H):
                        if board[ny + j][nx:nx + W] != [0] * W:
                            flag = 0
                            break
                    if flag:
                        q.append([ny, nx, cnt + 1])
                        visit[ny][nx] = 1
        q.popleft()
    print(ans)


if __name__ == '__main__':
    main()
