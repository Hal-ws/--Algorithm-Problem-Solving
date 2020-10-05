from collections import deque
import sys


def main():
    N = int(sys.stdin.readline())
    town = []
    maxHeight = 0
    minHeight = 101
    for i in range(N):
        town.append(list(map(int, sys.stdin.readline().split())))
        tempMax = max(town[i])
        tempMin = min(town[i])
        if tempMax > maxHeight:
            maxHeight = tempMax
        if tempMin < minHeight:
            minHeight = tempMin
    ans = 0
    for i in range(minHeight - 1, maxHeight):
        temp = getarea(town, i, N)
        if temp > ans:
            ans = temp
    print(ans)


def getarea(town, height, N):
    visited = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if town[i][j] <= height:
                town[i][j] = 0
                visited[i][j] = 1
    q = deque()
    safe = 0
    for i in range(N):
        for j in range(N):
            if town[i][j] != 0 and visited[i][j] == 0:
                q.append([i, j])
                visited[i][j] = 1
                safe += 1
                while len(q) > 0:
                    if q[0][0] > 0 and town[q[0][0] - 1][q[0][1]] != 0 and visited[q[0][0] - 1][q[0][1]] == 0:
                        q.append([q[0][0] - 1, q[0][1]])
                        visited[q[0][0] - 1][q[0][1]] = 1
                    if q[0][0] < N - 1 and town[q[0][0] + 1][q[0][1]] != 0 and visited[q[0][0] + 1][q[0][1]] == 0:
                        q.append([q[0][0] + 1, q[0][1]])
                        visited[q[0][0] + 1][q[0][1]] = 1
                    if q[0][1] > 0 and town[q[0][0]][q[0][1] - 1] != 0 and visited[q[0][0]][q[0][1] - 1] == 0:
                        q.append([q[0][0], q[0][1] - 1])
                        visited[q[0][0]][q[0][1] - 1] = 1
                    if q[0][1] < N - 1 and town[q[0][0]][q[0][1] + 1] != 0 and visited[q[0][0]][q[0][1] + 1] == 0:
                        q.append([q[0][0], q[0][1] + 1])
                        visited[q[0][0]][q[0][1] + 1] = 1
                    q.popleft()

    return safe


if __name__ == "__main__":
    main()
