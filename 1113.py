import sys
from collections import deque


def main():
    global N, M
    N, M = map(int, sys.stdin.readline().split())
    minH, maxH = 10, 0
    pool = [[[0 for j in range(M)] for i in range(N)] for k in range(10)]
    for i in range(N):
        tmp = list(map(int, sys.stdin.readline()[:M]))
        for j in range(M):
            if tmp[j] <= minH:
                minH = tmp[j]
            if tmp[j] >= maxH:
                maxH = tmp[j]
            for k in range(tmp[j] + 1):
                pool[k][i][j] = 1 #물 채워넣음
    answer = 0
    for height in range(minH + 1, maxH + 1):
        answer += getArea(pool[height])
    print(answer)


def getArea(layer):
    global N, M
    q = deque()
    visited = [[0 for j in range(M)] for i in range(N)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if i == 0 or j == 0 or i == N - 1 or j == M - 1:
                if layer[i][j] == 0:# 바깥쪽이랑 무조건 연결됨
                    q.append([i, j])
                    layer[i][j] = -1
                    visited[i][j] = 1
    while len(q) > 0: #layer에서 바깥쪽 연결된 곳에 표시
        curY, curX = q[0][0], q[0][1]
        for i in range(4):
            nY, nX = curY + dy[i], curX + dx[i]
            if 0 <= nY < N and 0 <= nX < M:
                if layer[nY][nX] == 0 and visited[nY][nX] == 0:
                    layer[nY][nX] = -1 #밖으로 빠져나감
                    q.append([nY, nX])
                    visited[nY][nX] = 1
        q.popleft()
    q = deque()
    for i in range(N):
        for j in range(M):
            if layer[i][j] == 1:
                q.append([i, j])
                visited[i][j] = 1
    while len(q) > 0:
        curY, curX = q[0][0], q[0][1]
        for i in range(4):
            nY, nX = curY + dy[i], curX + dx[i]
            if 0 <= nY < N and 0 <= nX < M:
                if layer[nY][nX] == 0 and visited[nY][nX] == 0:
                    cnt += 1
                    visited[nY][nX] = 1
                    q.append([nY, nX])
        q.popleft()
    return cnt


if __name__ == "__main__":
    main()
