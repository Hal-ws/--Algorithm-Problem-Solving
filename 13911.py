import sys
from queue import PriorityQueue
from math import inf


def main():
    global connect, macDis, starDis, x, y
    V, E = map(int, sys.stdin.readline().split())
    ans = inf
    connect = [[] for i in range(V)]
    macDis = [inf] * V
    starDis = [inf] * V
    for i in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        connect[u - 1].append([v - 1, w])
        connect[v - 1].append([u - 1, w])
    M, x = map(int, sys.stdin.readline().split())
    mac = list(map(int, sys.stdin.readline().split()))
    for i in range(M):
        mac[i] -= 1
        getDis(mac[i], 1)
    S, y = map(int, sys.stdin.readline().split())
    star = list(map(int, sys.stdin.readline().split()))
    for i in range(S):
        star[i] -= 1
        getDis(star[i], 0)
    for i in range(V):
        if macDis[i] <= x and starDis[i] <= y and macDis[i] + starDis[i] < ans:
            ans = macDis[i] + starDis[i]
    if ans == inf:
        print(-1)
    else:
        print(ans)


def getDis(pos, flag): # macdis인지, starDis인지 구별
    global connect, macDis, starDis, x, y
    q = PriorityQueue()
    q.put([0, pos])
    if flag:
        macDis[pos] = 0
    else:
        starDis[pos] = 0
    while q.empty() != True:
        tmp = q.get()
        dis, cur = tmp[0], tmp[1]
        for nxt in connect[cur]:
            nxtP, tDis = nxt[0], dis + nxt[1]
            if flag:
                if tDis <= x and tDis < macDis[nxtP]: # 맥세권일때
                    macDis[nxtP] = tDis
                    q.put([tDis, nxtP])
            else:
                if tDis <= y and tDis < starDis[nxtP]:
                    starDis[nxtP] = tDis
                    q.put([tDis, nxtP])


if __name__ == '__main__':
    main()
