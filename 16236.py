import sys
from collections import deque


def main():
    N = int(sys.stdin.readline())
    sea = [0] * N
    cnt = 0
    for i in range(N):
        sea[i] = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                baby = [i, j, 2, 0] # 상어 위치, 크기, 먹은 물고기수
    while True:
        add = findtarget(sea, baby, N)
        if add == 0:
            break
        if baby[2] == baby[3]:
            baby[2] += 1
            baby[3] = 0
        cnt += add
    print(cnt)


def findtarget(sea, baby, N):
    visit = [[0 for i in range(N)] for j in range(N)]
    visit[baby[0]][baby[1]] = 1
    dis = [[0 for i in range(N)] for j in range(N)]
    edible = []
    q = deque()
    q.append([baby[0], baby[1]])
    while len(q) > 0:
        if q[0][0] > 0 and sea[q[0][0] - 1][q[0][1]] <= baby[2] and visit[q[0][0] - 1][q[0][1]] == 0:
            q.append([q[0][0] - 1, q[0][1]])
            visit[q[0][0] - 1][q[0][1]] = 1
            dis[q[0][0] - 1][q[0][1]] = dis[q[0][0]][q[0][1]] + 1
        if q[0][1] < N - 1 and sea[q[0][0]][q[0][1] + 1] <= baby[2] and visit[q[0][0]][q[0][1] + 1] == 0:
            q.append([q[0][0], q[0][1] + 1])
            visit[q[0][0]][q[0][1] + 1] = 1
            dis[q[0][0]][q[0][1] + 1] = dis[q[0][0]][q[0][1]] + 1
        if q[0][0] < N - 1 and sea[q[0][0] + 1][q[0][1]] <= baby[2] and visit[q[0][0] + 1][q[0][1]] == 0:
            q.append([q[0][0] + 1, q[0][1]])
            visit[q[0][0] + 1][q[0][1]] = 1
            dis[q[0][0] + 1][q[0][1]] = dis[q[0][0]][q[0][1]] + 1
        if q[0][1] > 0 and sea[q[0][0]][q[0][1] - 1] <= baby[2] and visit[q[0][0]][q[0][1] - 1] == 0:
            q.append([q[0][0], q[0][1] - 1])
            visit[q[0][0]][q[0][1] - 1] = 1
            dis[q[0][0]][q[0][1] - 1] = dis[q[0][0]][q[0][1]] + 1
        if 0 < sea[q[0][0]][q[0][1]] < baby[2] and sea[q[0][0]][q[0][1]] != 9:
            edible.append([dis[q[0][0]][q[0][1]], q[0][0], q[0][1]])
        del q[0]
    if len(edible) == 0:
        return 0
    edible.sort()
    target = edible[0]
    sea[baby[0]][baby[1]] = 0
    baby[0], baby[1], baby[3] = target[1], target[2], (baby[3] + 1)
    sea[baby[0]][baby[1]] = 9
    return dis[target[1]][target[2]]


if __name__ == "__main__":
    main()
