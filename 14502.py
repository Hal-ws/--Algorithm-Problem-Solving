from itertools import combinations
from collections import deque
import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    room, empty, virus, ans, wallcnt = [0] * N, [], [], 64, 0
    for i in range(N):
        room[i] = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        for j in range(M):
            if room[i][j] == 0:
                empty.append([i, j])
            if room[i][j] == 2:
                virus.append([i, j])
            if room[i][j] == 1:
                wallcnt += 1
    cases = list(combinations(empty, 3))
    lc = len(cases)
    for i in range(lc):
        danger = getarea(room, cases[i], virus, N, M)
        if danger <= ans:
            ans = danger
    print(N * M - (wallcnt + 3) - ans)


def getarea(room, wall, virus, N, M):
    q = deque()
    cnt = len(virus)
    visit = [[0 for i in range(M)] for j in range(N)]
    for i in range(3):
        room[wall[i][0]][wall[i][1]] = 1
    for i in range(cnt):
        q.append(virus[i])
        visit[virus[i][0]][virus[i][1]] = 1
    while len(q) > 0:
        if q[0][0] > 0 and visit[q[0][0] - 1][q[0][1]] == 0 and room[q[0][0] - 1][q[0][1]] == 0:
            q.append([q[0][0] - 1, q[0][1]])
            visit[q[0][0] - 1][q[0][1]] = 1
            cnt += 1
        if q[0][0] < N - 1 and visit[q[0][0] + 1][q[0][1]] == 0 and room[q[0][0] + 1][q[0][1]] == 0:
            q.append([q[0][0] + 1, q[0][1]])
            visit[q[0][0] + 1][q[0][1]] = 1
            cnt += 1
        if q[0][1] > 0 and visit[q[0][0]][q[0][1] - 1] == 0 and room[q[0][0]][q[0][1] - 1] == 0:
            q.append([q[0][0], q[0][1] - 1])
            visit[q[0][0]][q[0][1] - 1] = 1
            cnt += 1
        if q[0][1] < M - 1 and visit[q[0][0]][q[0][1] + 1] == 0 and room[q[0][0]][q[0][1] + 1] == 0:
            q.append([q[0][0], q[0][1] + 1])
            visit[q[0][0]][q[0][1] + 1] = 1
            cnt += 1
        del q[0]
    for i in range(3):
        room[wall[i][0]][wall[i][1]] = 0
    return cnt


if __name__ == "__main__":
    main()
