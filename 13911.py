import sys
from math import inf
from queue import PriorityQueue


def main():
    global connect, x, y, macDis, starDis, chk
    V, E = map(int, sys.stdin.readline().split())
    connect = [[] for i in range(V + 1)]
    chk = [[0, 0] for i in range(V + 1)]
    macDis, starDis = [inf] * (V + 1), [inf] * (V + 1)
    ans = inf
    for i in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        connect[u].append([v, w])
        connect[v].append([u, w])
    M, x = map(int, sys.stdin.readline().split())
    macPos = list(map(int, sys.stdin.readline().split()))
    S, y = map(int, sys.stdin.readline().split())
    starPos = list(map(int, sys.stdin.readline().split()))
    for i in range(M):
        chk[macPos[i]][0] = 1
    for i in range(S):
        chk[starPos[i]][1] = 1
    for i in range(1, V + 1):
        if chk[i][0] == 1 and macDis[i] != 0:
            getdis(i)
        if chk[i][1] == 1 and starDis[i] != 0:
            getdis(i)
    for i in range(1, V + 1):
        mD, sD = macDis[i], starDis[i]
        if mD != 0 and sD != 0: # 맥도날드도, 스타벅스도 아닌 장소
            if mD <= x and sD <= y and mD + sD < ans:
                ans = mD + sD
    if ans == inf:
        print(-1)
    else:
        print(ans)


def getdis(pos):
    global connect, x, y, macDis, starDis, chk
    q = PriorityQueue()
    if chk[pos][0] == 1:
        macDis[pos] = 0
        q.put([0, pos, 0]) # 0 or 1: mac으로부터 거리, star로부터 거리
    if chk[pos][1] == 1:
        starDis[pos] = 0
        q.put([0, pos, 1])
    while q.empty() != True:
        tmp = q.get()
        dis, cur, flag = tmp[0], tmp[1], tmp[2]
        for nxt in connect[cur]:
            nxtP, tDis = nxt[0], dis + nxt[1]
            if chk[nxtP][0] == 0 and chk[nxtP][1] == 0: # 일반 집 방문
                if flag: # 스타벅스로부터 거리 구하고 있을때
                    if tDis < starDis[nxtP] and tDis <= y:
                        starDis[nxtP] = tDis
                        q.put([tDis, nxtP, 1])
                else: # 맥도날드로부터 거리 구하고 있을때
                    if tDis < macDis[nxtP] and tDis <= x:
                        macDis[nxtP] = tDis
                        q.put([tDis, nxtP, 0])
            else:
                if chk[nxtP][0] == 1: # 맥도날드 방문
                    if macDis[nxtP] != 0:
                        macDis[nxtP] = 0
                        q.put([0, nxtP, 0])
                    if flag: # 스타벅스로부터의 거리 구하고 있을때
                        if tDis < starDis[nxtP] and tDis <= y:
                            starDis[nxtP] = tDis
                            q.put([tDis, nxtP, 1])
                if chk[nxtP][1] == 1: # 스타벅스 방문
                    if starDis[nxtP] != 0:
                        starDis[nxtP] = 0
                        q.put([0, nxtP, 1])
                    if flag == 0: # 맥도날드로부터 거리 구하고 있을 때
                        if tDis < macDis[nxtP] and tDis <= x:
                            macDis[nxtP] = tDis
                            q.put([tDis, nxtP, 0])


if __name__ == '__main__':
    main()
