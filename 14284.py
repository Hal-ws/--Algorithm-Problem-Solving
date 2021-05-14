import sys
from math import inf
import heapq


def main():
    global n, m
    n, m = map(int, sys.stdin.readline().split())
    connect = [[] for i in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        connect[a].append([b, c])
        connect[b].append([a, c])
    s, t = map(int, sys.stdin.readline().split())
    print(daikstra(connect, s, t))


def daikstra(connect, s, t):
    global n, m
    distance = [inf for i in range(n + 1)]
    h = []
    distance[s] = 0
    heapq.heappush(h, [0, s]) # 거리, 위치 저장
    while len(h) > 0:
        tmp = heapq.heappop(h)
        cDis, pos = tmp[0], tmp[1]
        for nxt in connect[pos]:
            nxtP, tDis = nxt[0], cDis + nxt[1]
            if tDis < distance[nxtP]:
                distance[nxtP] = tDis
                heapq.heappush(h, [tDis, nxtP])
    return distance[t]


if __name__ == '__main__':
    main()
