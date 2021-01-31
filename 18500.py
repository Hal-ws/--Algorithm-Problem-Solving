import sys
from collections import deque


def main():
    global R, C, board, dy, dx
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    board = []
    R, C = map(int, sys.stdin.readline().split())
    for i in range(R):
        board.append(list(sys.stdin.readline()[:C]))
    N = int(sys.stdin.readline())
    tList = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        y = R - tList[i]
        throwing(y, i % 2)
    for i in range(R):
        for j in range(C):
            print(board[i][j], end='')
        print()


def throwing(y, d): #d가 0: 왼쪽에서 던짐. d가 1: 오른쪽에서 던짐
    global R, C, board, cluster
    cluster = [[0 for j in range(C)] for i in range(R)]
    flag1 = 0
    flag2 = 0
    if d:
        for j in range(C - 1, -1, -1):
            if board[y][j] == 'x':
                board[y][j] = '.'
                flag1 = 1
                break
    else:
        for j in range(C):
            if board[y][j] == 'x':
                board[y][j] = '.'
                flag1 = 1
                break
    if flag1:
        for j in range(C):
            if board[R - 1][j] == 'x' and cluster[R - 1][j] == 0: #바닥에 붙은 클러스터
                bfs(R - 1, j, 1)
        for i in range(R - 1):
            for j in range(C):
                if board[i][j] == 'x' and cluster[i][j] == 0:
                    bfs(i, j, 2)
                    flag2 = 1
    if flag2:
        falling()


def falling():
    global R, C, board, cluster
    minDis = 101
    for j in range(C):
        i = 0
        while i < R:
            if cluster[i][j] == 2: #공중에 떠있음
                flag = 0 # 거리 측정 가능한지 확인
                if cluster[i + 1][j] == 0: #빈칸이 있을때 거리 측정 시작
                    for ni in range(i + 2, R):
                        if cluster[ni][j] == 1:
                            flag = 1
                            d = ni - i - 1
                            break
                        elif cluster[ni][j] == 2:
                            break
                        elif ni == R - 1:
                            flag = 1
                            d = ni - i
                            break
                elif cluster[i + 1][j] == 1:
                    flag = 1
                    d = 0
                if flag:
                    i += (d + 2)
                    if d < minDis:
                        minDis = d
                else:
                    i += 1
            else:
                i += 1
    for j in range(C):
        for i in range(R - 1, -1, -1):
            if cluster[i][j] == 2:
                board[i + minDis][j] = 'x'
                board[i][j] = '.'

            
def bfs(y, x, cnt):
    global R, C, board, cluster, dy, dx
    q = deque()
    q.append([y, x])
    cluster[y][x] = cnt
    while len(q) > 0:
        y, x = q[0][0], q[0][1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < R and 0 <= nx < C and cluster[ny][nx] == 0 and board[ny][nx] == 'x':
                cluster[ny][nx] = cnt
                q.append([ny, nx])
        q.popleft()


if __name__ == "__main__":
    main()
