import sys
from collections import deque


def main():
    N, M = map(int, sys.stdin.readline().split())
    ice = []
    for i in range(N):
        ice.append(list(map(int, sys.stdin.readline().split())))
    day = 0
    while 1:
        ice = melt(ice, N, M)
        pieces = bfs(ice, N, M)
        day += 1
        if pieces > 1:
            break
        if pieces == 0: ## 두조각 나지 않고 그냥 녹아버린 경우
            day = 0
            break
    print(day)


def bfs(ice, N, M):
    visited = [[0 for i in range(M)] for j in range(N)]
    piece = 0
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0 and visited[i][j] == 0:
                piece += 1
                q = deque()
                q.append([i, j])
                visited[i][j] = 1
                while len(q) > 0:
                    if q[0][0] > 0:
                        if ice[q[0][0] - 1][q[0][1]] != 0 and visited[q[0][0] - 1][q[0][1]] == 0:
                            q.append([q[0][0] - 1, q[0][1]])
                            visited[q[0][0] - 1][q[0][1]] = 1
                    if q[0][0] < N - 1:
                        if ice[q[0][0] + 1][q[0][1]] != 0 and visited[q[0][0] + 1][q[0][1]] == 0:
                            q.append([q[0][0] + 1, q[0][1]])
                            visited[q[0][0] + 1][q[0][1]] = 1
                    if q[0][1] > 0:
                        if ice[q[0][0]][q[0][1] - 1] != 0 and visited[q[0][0]][q[0][1] - 1] == 0:
                            q.append([q[0][0], q[0][1] - 1])
                            visited[q[0][0]][q[0][1] - 1] = 1
                    if q[0][1] < M - 1:
                        if ice[q[0][0]][q[0][1] + 1] != 0 and visited[q[0][0]][q[0][1] + 1] == 0:
                            q.append([q[0][0], q[0][1] + 1])
                            visited[q[0][0]][q[0][1] + 1] = 1
                    q.popleft()
    return piece


def melt(ice, N, M):
    meltCnt = [[0 for i in range(M)] for j in range(N)]
    for i in range(N):
        for j in range(M):
            mltcnt = 0
            if ice[i][j] != 0:
                if i > 0 and ice[i - 1][j] == 0:
                    mltcnt += 1
                if i < N - 1 and ice[i + 1][j] == 0:
                    mltcnt += 1
                if j > 0 and ice[i][j - 1] == 0:
                    mltcnt += 1
                if j < M - 1 and ice[i][j + 1] == 0:
                    mltcnt += 1
            meltCnt[i][j] = mltcnt
    for i in range(N):
        for j in range(M):
            if meltCnt[i][j] > 0:
                ice[i][j] -= meltCnt[i][j]
                if ice[i][j] < 0:
                    ice[i][j] = 0
    return ice


if __name__ == "__main__":
    main()
