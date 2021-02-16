import sys
from collections import deque


def main():
    global N, board, rChk, hChk, vChk
    N = int(sys.stdin.readline())
    board = []
    rChk = [[0 for j in range(N)] for i in range(N)] # 회전 가능한지 체크
    vChk = [[0 for j in range(N)] for i in range(N)] # 수직 가능한지 체크
    hChk = [[0 for j in range(N)] for i in range(N)] # 수평 가능한지 체크
    for i in range(N):
        board.append(list(sys.stdin.readline()[:N]))
    start, target = [], []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'B':
                start.append([i, j])
            if board[i][j] == 'E':
                target.append([i, j])
            if i == 0 or i == N - 1:
                if 1 <= j < N - 1:
                    if board[i][j] != '1' and board[i][j - 1] != '1' and board[i][j + 1] != '1':
                        hChk[i][j] = 1
            if j == 0 or j == N - 1:
                if 1 <= i < N - 1:
                    if board[i - 1][j] != '1' and board[i][j] != '1' and board[i + 1][j] != '1':
                        vChk[i][j] = 1
            if 1 <= i <= N - 2 and 1 <= j <= N - 2:
                rFlag = 0
                vFlag = 1
                hFlag = 1
                for k in range(i - 1, i + 2): # 수직
                    if board[k][j] == '1':
                        vFlag = 0
                        break
                for k in range(j - 1, j + 2): # 수평
                    if board[i][k] == '1':
                        hFlag = 0
                        break
                if vFlag == hFlag == 1:
                    if board[i - 1][j - 1] != '1' and board[i - 1][j + 1] != '1' and board[i + 1][j - 1] != '1' and board[i + 1][j + 1] != '1':
                        rFlag = 1
                if vFlag:
                    vChk[i][j] = 1
                if hFlag:
                    hChk[i][j] = 1
                if rFlag:
                    rChk[i][j] = 1
    if start[0][0] == start[1][0] == start[2][0]:
        s = 0 # 가로
    else:
        s = 1 # 세로
    if target[0][0] == target[1][0] == target[2][0]:
        e = 0
    else:
        e = 1
    print(bfs(start[1], target[1], s, e))


def bfs(sPos, ePos, start, target):
    global N, board, rChk, hChk, vChk
    visit = [[[0 for j in range(N)] for i in range(N)] for k in range(2)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    y, x = sPos[0], sPos[1]
    q = deque()
    visit[start][y][x] = 1
    q.append([y, x, start, 0])
    while len(q) > 0:
        y, x, state, cnt = q[0][0], q[0][1], q[0][2], q[0][3]
        if y == ePos[0] and x == ePos[1] and state == target:
            return cnt
        for i in range(4): #평행이동
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N: # 평행이동 가능한지 확인
                if visit[state][ny][nx] == 0:
                    if state == 0 and hChk[ny][nx]: # 수평
                        visit[state][ny][nx] = 1
                        q.append([ny, nx, state, cnt + 1])
                    if state == 1 and vChk[ny][nx]:
                        visit[state][ny][nx] = 1
                        q.append([ny, nx, state, cnt + 1])
        if rChk[y][x]:
            if state == 0 and visit[1][y][x] == 0:
                visit[1][y][x] = 1
                q.append([y, x, 1, cnt + 1])
            if state == 1 and visit[0][y][x] == 0:
                visit[0][y][x] = 1
                q.append([y, x, 0, cnt + 1])
        q.popleft()
    return 0

if __name__ == '__main__':
    main()
