import sys
import heapq
from math import inf


def main():
    n, m = map(int, sys.stdin.readline().split())
    connect = [[] for i in range(n + 1)]
    for _ in range(m):
        p1, p2, dis = map(int, sys.stdin.readline().split())
        connect[p1].append([p2, dis])
        connect[p2].append([p1, dis])
    answer = [[None for j in range(n + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        daikstra(i, answer, connect, n)
        answer[i][i] = '-'
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(answer[i][j], end=' ')
        print()


def daikstra(start, answer, connect, n):
    distance = [inf for i in range(n + 1)]
    distance[start] = 0
    hq = []
    heapq.heappush(hq, [0, start, None]) # 거리, 좌표, 최초 이동장소 기록
    while len(hq) > 0:
        tmp = heapq.heappop(hq)
        cDis, pos, fPlace = tmp[0], tmp[1], tmp[2]
        for nxt in connect[pos]:
            nxtP, dis = nxt[0], nxt[1] + cDis
            if fPlace == None: # 최초로 이동하는곳
                answer[start][nxtP] = nxtP
            if dis < distance[nxtP]: # 거리 갱신
                if fPlace != None:
                    answer[start][nxtP] = fPlace
                    heapq.heappush(hq, [dis, nxtP, fPlace])
                else:
                    heapq.heappush(hq, [dis, nxtP, nxtP])
                distance[nxtP] = dis


if __name__ == "__main__":
    main()
