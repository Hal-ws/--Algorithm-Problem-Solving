import sys
import heapq
from math import inf



def main():
    N, M = map(int, sys.stdin.readline().split())
    connect = [[] for i in range(N + 1)]
    for _ in range(M):
        a, b, d = map(int, sys.stdin.readline().split())
        connect[a].append([b, d])
        connect[b].append([a, d])
    foxDis = [inf] * (N + 1)
    wolfDis = [[inf] * (N + 1) for i in range(2)]
    foxDis[1], wolfDis[0][1] = 0, 0  # 0일 때는 2배 속도로 이동가능
    hq = []
    heapq.heappush(hq, [0, 1])
    ## 달빛 여우 먼저
    while len(hq) > 0:
        tmp = heapq.heappop(hq)
        cDis, node = tmp[0], tmp[1]
        for nxt in connect[node]:
            nxtNode, tDis = nxt[0], nxt[1] + cDis
            if tDis < foxDis[nxtNode]: # 더 짧게 도달가능
                foxDis[nxtNode] = tDis
                heapq.heappush(hq, [tDis, nxtNode])
    hq = []
    heapq.heappush(hq, [0, 1, 0])  #
    while len(hq) > 0:
        tmp = heapq.heappop(hq)
        cDis, node, state = tmp[0], tmp[1], tmp[2]
        for nxt in connect[node]:
            nxtNode, dis = nxt[0], nxt[1]
            if state == 0: # 2배 속도로 이동
                tDis = cDis + dis / 2
            else: # 1/2 속도로 이동
                tDis = cDis + dis * 2
            newState = (state + 1) % 2
            if tDis < wolfDis[newState][nxtNode]:
                wolfDis[newState][nxtNode] = tDis
                heapq.heappush(hq, [tDis, nxtNode, newState])
    answer = 0
    for i in range(1, N + 1):
        if foxDis[i] < min(wolfDis[0][i], wolfDis[1][i]):
            answer += 1
    print(answer)


if __name__ == "__main__":
    main()
