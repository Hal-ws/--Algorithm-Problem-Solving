import sys
from _collections import deque


def main():
    global N, M, hBoard, maxH
    N, M = map(int, sys.stdin.readline().split())
    hBoard = []
    maxH = 0
    answer = 0
    for i in range(N):
        hBoard.append(list(map(int, sys.stdin.readline().split())))
        tmpMaxH = max(hBoard[-1])
        if maxH < tmpMaxH:
            maxH = tmpMaxH
    for stdH in range(maxH + 1):
        answer += water(stdH)
    print(answer)


def water(stdH):
    global N, M, hBoard, maxH
    visit = [[0 for j in range(M)] for i in range(N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if hBoard[i][j] > stdH:
                visit[i][j] = 1
    for i in range(N):
        for j in range(M):
            if i == 0 or i == N - 1 or j == 0 or j == M - 1:
                if visit[i][j] == 0: # 물이 찰 수 있는 공간
                    q = deque()
                    visit[i][j] = 1
                    q.append([i, j])
                    while len(q) > 0:
                        tmp = q.popleft()
                        y, x = tmp[0], tmp[1]
                        for k in range(4):
                            ny, nx = y + dy[k], x + dx[k]
                            if 0 <= ny < N and 0 <= nx < M and visit[ny][nx] == 0:
                                visit[ny][nx] = 1
                                q.append([ny, nx])
    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0:
                cnt += 1
    return cnt


if __name__ == '__main__':
    main()
