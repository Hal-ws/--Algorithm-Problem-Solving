from collections import deque
import sys


def main():
    global N, M
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    t = 0
    while 1:
        t += 1
        tmp = bfs(board) #치즈가 공기에 얼마나 노출됐는지 확인후 치즈 녹임
        if tmp == 0:
            print(t)
            break


def bfs(board):
    global N, M
    exposed = [[0 for j in range(M)] for i in range(N)]
    visited = [[0 for j in range(M)] for i in range(N)]
    start = [0, 0] #
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    q.append(start)
    visited[0][0] = 1
    while len(q) > 0:
        curY, curX = q[0][0], q[0][1]
        for i in range(4):
            nxtY, nxtX = curY + dy[i], curX + dx[i]
            if 0 <= nxtY < N and 0 <= nxtX < M:
                if visited[nxtY][nxtX] == 0:
                    if board[nxtY][nxtX] == 0:
                        q.append([nxtY, nxtX])
                        visited[nxtY][nxtX] = 1
                    else:
                        exposed[nxtY][nxtX] += 1
        q.popleft()
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cnt += 1
                if exposed[i][j] >= 2:
                    board[i][j] = 0
                    cnt -= 1
    if cnt == 0:
        return 0
    else:
        return 1



if __name__ == '__main__':
    main()
