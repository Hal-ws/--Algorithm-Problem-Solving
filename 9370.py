import sys
import heapq
from math import inf



def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n, m, t = map(int, sys.stdin.readline().split()) # 도시 수, 도로 수, 목적지 후보 수
        s, g, h = map(int, sys.stdin.readline().split())
        connect = [[] for i in range(n + 1)]
        for i in range(m):
            a, b, d = map(int, sys.stdin.readline().split())
            connect[a].append([b, d])
            connect[b].append([a, d])
        targets = []
        for i in range(t):
            targets.append(int(sys.stdin.readline()))
        targets.sort()
        path = daikstra(n, connect, s, g, h) # targets 에 있는 path들 중 g-h or h-g 가 있는지 확인해 봐야한다
        for t in targets:
            if path[t][1]:
                print(t, end=' ')


def daikstra(n, connect, start, g, h):
    distance = [inf for i in range(n + 1)] #
    path = [['', 0] for i in range(n + 1)] # i번 도시에 도착하기 위한 path 저장. g - h 또는 h - g를 포함하는지 표시
    distance[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])
    path[start][0] = str(start)
    while len(heap) > 0:
        tmp = heapq.heappop(heap)
        cDis, curP = tmp[0], tmp[1]
        for nxt in connect[curP]:
            nxtP, nxtD = nxt[0], nxt[1]
            flag = 0
            if (curP == g and nxtP == h) or (curP == h and nxtP == g) or path[curP][1]:
                flag = 1
            if cDis + nxtD < distance[nxtP]: # nxtP로 가는 path 업데이트
                distance[nxtP] = cDis + nxtD
                path[nxtP] = [path[curP][0] + str(nxtP), flag]
                heapq.heappush(heap, [cDis + nxtD, nxtP])
            if cDis + nxtD == distance[nxtP]:
                if path[nxtP][1] == 0 and flag:
                    distance[nxtP] = cDis + nxtD
                    path[nxtP] = [path[curP][0] + str(nxtP), flag]
                    heapq.heappush(heap, [cDis + nxtD, nxtP])
    return path


if __name__ == '__main__':
    main()
