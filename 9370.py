import sys
import heapq
from math import inf



def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n, m, t = map(int, sys.stdin.readline().split()) # 도시 수, 도로 수, 목적지 후보 수
        s, g, h = map(int, sys.stdin.readline().split())
        connect = [[] for i in range(n + 1)]
        strg, strh = str(g), str(h)
        for i in range(m):
            a, b, d = map(int, sys.stdin.readline().split())
            connect[a].append([b, d])
            connect[b].append([a, d])
        targets = []
        for i in range(t):
            targets.append(int(sys.stdin.readline()))
        targets.sort()
        path = daikstra(n, connect, s) # targets 에 있는 path들 중 g-h or h-g 가 있는지 확인해 봐야한다
        for t in targets:
            tPath = path[t]
            flag = 0
            for i in range(len(tPath) - 1):
                if (tPath[i] == strg and tPath[i + 1] == strh) or (tPath[i] == strh and tPath[i + 1] == strg):
                    flag = 1
                    break
            if flag:
                print(t, end=' ')


def daikstra(n, connect, start):
    distance = [inf for i in range(n + 1)] #
    path = ['' for i in range(n + 1)] # i번 도시에 도착하기 위한 path 저장
    distance[start] = 0
    heap = []
    heapq.heappush(heap, [0, start, 0])
    path[start] = str(start)
    while len(heap) > 0:
        tmp = heapq.heappop(heap)
        cDis, curP = tmp[0], tmp[1]
        for nxt in connect[curP]:
            nxtP, nxtD = nxt[0], nxt[1]
            if cDis + nxtD < distance[nxtP]:
                distance[nxtP] = cDis + nxtD
                path[nxtP] = path[curP] + str(nxtP)
                heapq.heappush(heap, [cDis + nxtD, nxtP])
    return path


if __name__ == '__main__':
    main()
