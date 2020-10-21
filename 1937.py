import sys
from queue import deque


def main():
    N = int(sys.stdin.readline())
    trees = []
    for i in range(N):
        trees.append(list(map(int, sys.stdin.readline().split())))
    lifeList = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if lifeList[i][j] == 0:
                bfs(trees, lifeList, [i, j], N)
    ans = 0
    for i in range(N):
        for j in range(N):
            if ans <= lifeList[i][j]:
                ans = lifeList[i][j]
    print(ans)


def bfs(trees, lifeList, panda, N):
    distance = [[-1 for i in range(N)] for j in range(N)] ## -1: 아직 방문 안했음. 방문한거랑 거리를 한 행렬로 표현
    q = deque()
    q.append([panda[0], panda[1], 0])
    distance[panda[0]][panda[1]] = 0
    while 1:
        if q[0][0] > 0:
            if distance[q[0][0] - 1][q[0][1]] == -1 and trees[q[0][0] - 1][q[0][1]] > trees[q[0][0]][q[0][1]]:
                q.append([q[0][0] - 1, q[0][1], q[0][2] + 1])
                distance[q[0][0] - 1][q[0][1]] = q[0][2] + 1
        if q[0][0] < N - 1:
            if distance[q[0][0] + 1][q[0][1]] == -1 and trees[q[0][0] + 1][q[0][1]] > trees[q[0][0]][q[0][1]]:
                q.append([q[0][0] + 1, q[0][1], q[0][2] + 1])
                distance[q[0][0] + 1][q[0][1]] = q[0][2] + 1
        if q[0][1] > 0:
            if distance[q[0][0]][q[0][1] - 1] == -1 and trees[q[0][0]][q[0][1] - 1] > trees[q[0][0]][q[0][1]]:
                q.append([q[0][0], q[0][1] - 1, q[0][2] + 1])
                distance[q[0][0]][q[0][1] - 1] = q[0][2] + 1
        if q[0][1] < N - 1:
            if distance[q[0][0]][q[0][1] + 1] == -1 and trees[q[0][0]][q[0][1] + 1] > trees[q[0][0]][q[0][1]]:
                q.append([q[0][0], q[0][1] + 1, q[0][2] + 1])
                distance[q[0][0]][q[0][1] + 1] = q[0][2] + 1
        if len(q) == 1:
            maxDis = q[0][2]
            break
        q.popleft()
    for i in range(N):
        for j in range(N):
            if distance[i][j] != -1 and lifeList[i][j] == 0:
                lifeList[i][j] = maxDis - distance[i][j] + 1

    for i in range(N):
        print(lifeList[i])
    print('---------------------------------')

if __name__ == "__main__":
    main()
