import sys
from collections import deque


def main():
    global board, N, M, H, W
    board = []
    N, M = map(int, sys.stdin.readline().split())
    visit = [[0 for j in range(M)] for i in range(N)]
    emptyChk = [[1 for j in range(M)] for i in range(N)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    ans = -1
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    H, W, Sr, Sc, Fr, Fc = map(int, sys.stdin.readline().split())
    Sr, Sc, Fr, Fc = Sr - 1, Sc - 1, Fr - 1, Fc - 1
    for i in range(N):
        for j in range(M):
            if N - H < i:
                emptyChk[i][j] = 0
            if M - W < j:
                emptyChk[i][j] = 0
            if board[i][j] == 1: # 벽이 있으면
                for k in range(i - H + 1, i + 1):
                    for l in range(j - W + 1, j + 1):
                        if 0 <= k < N and 0 <= l < M:
                            emptyChk[k][l] = 0
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
                    if emptyChk[ny][nx]:
                        q.append([ny, nx, cnt + 1])
                        visit[ny][nx] = 1
        q.popleft()
    print(ans)


if __name__ == '__main__':
    main()
