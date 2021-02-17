import sys
from collections import deque


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        board = []
        for i in range(5):
            board.append(list(sys.stdin.readline()[:9]))
        pCnt = 0
        for i in range(5):
            for j in range(9):
                if board[i][j] == 'o':
                    pCnt += 1
        if _ != T - 1:
            dummy = sys.stdin.readline()
        tmp = bfs(board, pCnt)
        print('%s %s' %(tmp[0], tmp[1]))


def bfs(board, pCnt):
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    dy2, dx2 = [-2, 2, 0, 0], [0, 0, -2 ,2]
    q = deque()
    q.append([board, 0, pCnt])
    minPin = 9
    minMove = 10000000000000
    while len(q) > 0:
        b, mCnt, pCnt = q[0][0], q[0][1], q[0][2]
        flag = 0
        for i in range(5):
            for j in range(9):
                if b[i][j] == 'o':
                    for k in range(4):
                        ny, nx = i + dy[k], j + dx[k]
                        if 0 <= ny < 5 and 0 <= nx < 9 and b[ny][nx] == 'o':
                            ny2, nx2 = i + dy2[k], j + dx2[k]
                            if 0 <= ny2 < 5 and 0 <= nx2 < 9 and b[ny2][nx2] == '.':
                                flag = 1
                                nb = [[b[l][m] for m in range(9)] for l in range(5)]
                                nb[i][j] = '.'
                                nb[ny][nx] = '.'
                                nb[ny2][nx2] = 'o'
                                q.append([nb, mCnt + 1, pCnt - 1])
        if flag == 0: #더 이동할 것 없음
            if pCnt < minPin:
                minPin = pCnt
                minMove = mCnt
            if pCnt == minPin and mCnt < minMove:
                minMove = mCnt
        q.popleft()
    return [minPin, minMove]


if __name__ == '__main__':
    main()
