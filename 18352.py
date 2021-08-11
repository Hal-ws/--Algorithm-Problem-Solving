import sys
from collections import deque


def main():
    N, M, K, X = map(int, sys.stdin.readline().split())
    connect = [[] for i in range(N + 1)]
    visit = [-1 for j in range(N + 1)]
    q = deque()
    q.append([X, 0])
    visit[X] = 0
    ans = []
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        connect[a].append(b)
    while len(q) > 0:
        tmp = q.popleft()
        curPos, dis = tmp[0], tmp[1]
        for nxtCity in connect[curPos]:
            if visit[nxtCity] == -1:
                q.append([nxtCity, dis + 1])
                visit[nxtCity] = dis + 1
    for city in range(1, N + 1):
        if visit[city] == K:
            ans.append(city)
    if len(ans) == 0:
        print(-1)
    else:
        for city in ans:
            print(city)


if __name__ == "__main__":
    main()
