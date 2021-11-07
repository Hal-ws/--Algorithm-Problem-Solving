import sys
from collections import deque


def main():
    N, M = map(int, sys.stdin.readline().split())
    connect = [[] for i in range(N + 1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        a, b = a - 1, b - 1
        connect[a].append(b)
        connect[b].append(a)
    visit = [0] * N
    distance = [0] * N
    q = deque()
    q.append([0, 0])
    visit[0] = 1
    maxDis = 0
    while len(q) > 0:
        tmp = q.popleft()
        cur, dis = tmp[0], tmp[1]
        maxDis = max(dis, maxDis)
        for nxt in connect[cur]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                distance[nxt] = dis + 1
                q.append([nxt, dis + 1])
    cnt = 0
    nearest = -1
    for i in range(N):
        if distance[i] == maxDis:
            cnt += 1
            if nearest == -1:
                nearest = i + 1
    print('%s %s %s' %(nearest, maxDis, cnt))


if __name__ == "__main__":
    main()
