import sys
import heapq
from math import inf


def main():
    N, M = map(int, sys.stdin.readline().split())
    connect = [[] for i in range(N + 1)]
    for i in range(M):
        A, B, C = map(int, sys.stdin.readline().split())
        connect[A].append([B, C])
        connect[B].append([A, C])
    lines = [[0 for j in range(N + 1)] for i in range(N + 1)]
    distance = [[inf, None] for i in range(N + 1)]
    distance[1][0] = 0
    hq = []
    heapq.heappush(hq, [0, 1])
    while len(hq) > 0:
        tmp = heapq.heappop(hq)
        cDis, curP = tmp[0], tmp[1]
        for nxt in connect[curP]:
            nxtP, tDis = nxt[0], cDis + nxt[1]
            if tDis < distance[nxtP][0]: # 거리가 더 짧음
                distance[nxtP][0] = tDis
                if distance[nxtP][1] != None: # 기존의 연결라인 삭제
                    node = distance[nxtP][1]
                    lines[node][nxtP] = 0
                    lines[nxtP][node] = 0
                lines[curP][nxtP] = 1
                lines[nxtP][curP] = 1
                distance[nxtP][1] = curP
                heapq.heappush(hq, [tDis, nxtP])
    print(N - 1)
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if lines[i][j]:
                print('%s %s' %(i, j))


if __name__ == "__main__":
    main()
