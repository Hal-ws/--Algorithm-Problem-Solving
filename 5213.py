import sys
from collections import deque


def main():
    global N, board, tileNum
    N = int(sys.stdin.readline())
    board = [[0 for j in range(N * 2)] for i in range(N)]
    tileNum = [[0 for j in range(N * 2)] for i in range(N)]
    l = 2 * N - 1
    if N % 2 == 1: #홀수일때
        totalTile = (N // 2 + 1) * N + (N // 2) * (N - 1)
    else:
        totalTile = (N // 2) * N + (N // 2) * (N - 1)
    for k in range(totalTile):
        a, b = map(int, sys.stdin.readline().split())
        iIdx = (k // l) * 2
        jIdx = k % l
        if jIdx >= N: # 홀수칸으로 빠짐
            iIdx += 1
            jIdx -= N
        if iIdx % 2 == 0:
            board[iIdx][jIdx * 2] = a
            board[iIdx][jIdx * 2 + 1] = b
            tileNum[iIdx][jIdx * 2] = k + 1
            tileNum[iIdx][jIdx * 2 + 1] = k + 1
        else:
            board[iIdx][jIdx * 2 + 1] = a
            board[iIdx][jIdx * 2 + 2] = b
            tileNum[iIdx][jIdx * 2 + 1] = k + 1
            tileNum[iIdx][jIdx * 2 + 2] = k + 1
    bfs()


def bfs():
    global N, board, tileNum
    visit = [[0 for j in range(N * 2)] for i in range(N)]
    dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
    maxTile = 1 #도착한 타일중 가장 큰 타일
    maxLen = 0 #가장 큰 타일에 도착했을때 길이
    nearPath = ''
    q = deque()
    visit[0][1] = 1
    visit[0][0] = 1
    q.append([1, '1', 0, 1]) # 지나간 칸수, path, y, x
    while len(q) > 0:
        tmp = q[0]
        cnt, path, y, x = tmp[0], tmp[1], tmp[2], tmp[3]
        if N % 2 == 1: #홀수일때
            if y == N - 1:
                if x == 2 * N - 1 or x == 2 * N - 2:
                    print(cnt)
                    print(path)
                    return
        else:
            if y == N - 1:
                if x == 2 * N - 2 or x == 2 * N - 3:
                    print(cnt)
                    print(path)
                    return
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < 2 * N and visit[ny][nx] == 0:
                if tileNum[y][x] != tileNum[ny][nx] and board[y][x] == board[ny][nx]: #다른 타일&같은숫자일때 이동
                    visit[ny][nx] = 1
                    q.append([cnt + 1, path + ' ' + str(tileNum[ny][nx]), ny, nx])
                    if 0 < nx and tileNum[ny][nx - 1] == tileNum[ny][nx] and visit[ny][nx - 1] == 0: # 붙어있는 타일도 이동시킨다
                        q.append([cnt + 1, path + ' ' + str(tileNum[ny][nx]), ny, nx - 1])
                        visit[ny][nx - 1] = 1
                    if nx < 2 * N - 1 and tileNum[ny][nx + 1] == tileNum[ny][nx] and visit[ny][nx + 1] == 0:
                        q.append([cnt + 1, path + ' ' + str(tileNum[ny][nx]), ny, nx + 1])
                        visit[ny][nx + 1] = 1
                    if maxTile < tileNum[ny][nx]:
                        maxTile = tileNum[ny][nx]
                        maxLen = cnt + 1
                        nearPath = path + ' ' + str(tileNum[ny][nx])
        q.popleft()
    print(maxLen)
    print(nearPath)
    return


if __name__ == '__main__':
    main()
