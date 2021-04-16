import sys
from _collections import deque
from math import inf


def main():
    global N, M, board, dy, dx, ans
    N, M = map(int, sys.stdin.readline().split())
    board = []
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    ans = inf
    minsik = None
    for i in range(N):
        board.append(list(sys.stdin.readline()[:M]))
        for j in range(M):
            if board[i][j] == '0':
                minsik = [i, j] #민식이 좌표
                board[i][j] = '.'
    bfs(minsik)
    if ans == inf:
        print(-1)
    else:
        print(ans)


def bfs(start):
    global N, M, board, dy, dx, ans
    visit = [[[0 for k in range(64)] for j in range(M)] for i in range(N)]
    q = deque()
    q.append([start[0], start[1], 0, 0]) # y, x, nxtKey(10진수로 저장)
    visit[start[0]][start[1]][0] = 1
    while len(q) > 0:
        tmp = q.popleft()
        y, x, curKey, cnt = tmp[0], tmp[1], tmp[2], tmp[3]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] != '#':
                if (board[ny][nx] == '.' or board[ny][nx] == '0') and visit[ny][nx][curKey] == 0:
                    if visit[ny][nx][curKey] == 0:
                        visit[ny][nx][curKey] = 1
                        q.append([ny, nx, curKey, cnt + 1])
                if 97 <= ord(board[ny][nx]) <= 102: # nxtKey get
                    nxtKey = curKey | pow(2, ord(board[ny][nx]) - 97)
                    if visit[ny][nx][nxtKey] == 0:
                        visit[ny][nx][nxtKey] = 1
                        q.append([ny, nx, nxtKey, cnt + 1])
                if 65 <= ord(board[ny][nx]) <= 70:
                    cmp = curKey | pow(2, ord(board[ny][nx]) - 65)
                    if curKey == cmp: # 이동가능함
                        if visit[ny][nx][curKey] == 0:
                            visit[ny][nx][curKey] = 1
                            q.append([ny, nx, curKey, cnt + 1])
                if board[ny][nx] == '1':
                    if cnt + 1 < ans:
                        ans = cnt + 1


if __name__ == '__main__':
    main()
