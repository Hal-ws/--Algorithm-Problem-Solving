import sys
from _collections import deque


def main():
    global N, M, K, board
    N, M, K = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(sys.stdin.readline()[:M]))
        for j in range(M):
            board[i][j] = int(board[i][j])
    print(bfs())


def bfs():
    global N, M, K, board
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visit = [[[0 for j in range(M)] for i in range(N)] for k in range(K + 1)]
    breakableCnt = [[0 for j in range(M)] for i in range(N)]
    q = deque()
    q.append([0, 0, K, 0, 1]) # y, x, 부술수 있는것, 날짜, 방문한 칸의 수
    visit[K][0][0] = 1
    breakableCnt[0][0] = K
    while len(q) > 0:
        print('q: %s' %q)
        tmp = q.popleft()
        y, x, possK, time, cnt = tmp[0], tmp[1], tmp[2], tmp[3], tmp[4]
        nxtD = (time + 1) % 2
        if y == N - 1 and x == M - 1:
            return cnt
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx] == 0 and visit[possK][ny][nx] == 0:
                    if breakableCnt[ny][nx] == 0 or breakableCnt[ny][nx] < possK:
                        visit[possK][ny][nx] = 1
                        breakableCnt[ny][nx] = possK
                        q.append([ny, nx, possK, nxtD, cnt + 1])
                if board[ny][nx] == 1 and time == 0 and possK > 0 and visit[possK - 1][ny][nx] == 0:
                    if breakableCnt[ny][nx] == 0 or breakableCnt[ny][nx] < possK:
                        visit[possK - 1][ny][nx] = 1
                        breakableCnt[ny][nx] = possK
                        q.append([ny, nx, possK - 1, nxtD, cnt + 1])
        if time == 1: # 밤일때는 하루 더 있어봐야함
            q.append([y, x, possK, nxtD, cnt + 1])
    return -1


if __name__ == '__main__':
    main()
