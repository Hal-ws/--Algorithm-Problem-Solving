import sys
from queue import PriorityQueue
from math import inf


def main():
    global connect, macDis, starDis, x, y, macChk, starChk
    V, E = map(int, sys.stdin.readline().split())
    ans = inf
    connect = [[] for i in range(V)]
    macDis = [inf] * V
    macChk = [0] * V
    starDis = [inf] * V
    starChk = [0] * V
    for i in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        connect[u - 1].append([v - 1, w])
        connect[v - 1].append([u - 1, w])
    M, x = map(int, sys.stdin.readline().split())
    mac = list(map(int, sys.stdin.readline().split()))
    S, y = map(int, sys.stdin.readline().split())
    star = list(map(int, sys.stdin.readline().split()))
    for i in range(M):
        mac[i] -= 1
        macChk[mac[i]] = 1
    for i in range(M):
        if macChk[mac[i]] == 1:
            getDis(mac[i], 1)
    for i in range(S):
        star[i] -= 1
        starChk[star[i]] = 1
    for i in range(S):
        if starChk[star[i]] == 1:
            getDis(star[i], 0)
    for i in range(V):
        mD, sD = macDis[i], starDis[i]
        if mD <= x and sD <= y and mD + sD < ans:
            if macChk[i] == 0 and starChk[i] == 0:
                ans = mD + sD
    if ans == inf:
        print(-1)
    else:
        print(ans)


def getDis(pos, flag): # macdis인지, starDis인지 구별
    global connect, macDis, starDis, x, y, macChk, starChk
    q = PriorityQueue()
    q.put([0, pos])
    if flag:
        macDis[pos] = 0
        macChk[pos] = 2
    else:
        starDis[pos] = 0
        starChk[pos] = 2
    while q.empty() != True:
        tmp = q.get()
        dis, cur = tmp[0], tmp[1]
        for nxt in connect[cur]:
            nxtP, tDis = nxt[0], dis + nxt[1]
            if flag: # 맥세권 찾는 프로세스
                if macChk[nxtP] and macDis[nxtP] > 0: # 다음 위치가 아직 맥세권 계산 안한 맥도날드일때
                    macDis[nxtP] = 0
                    q.put([0, nxtP])
                    macChk[nxtP] = 2
                elif macChk[nxtP] == 0: #
                    if tDis <= x and tDis < macDis[nxtP]: # 맥세권일때
                        macDis[nxtP] = tDis
                        q.put([tDis, nxtP])
            else: # 스세권 찾는 프로세스
                if starChk[nxtP] and starDis[nxtP] > 0: # 다음 위치가 아직 스세권 계산 안한 스타벅스일때
                    starDis[nxtP] = 0
                    q.put([0, nxtP])
                    starChk[nxtP] = 2
                elif starChk[nxtP] == 0:
                    if tDis <= y and tDis < starDis[nxtP]:
                        starDis[nxtP] = tDis
                        q.put([tDis, nxtP])


if __name__ == '__main__':
    main()
