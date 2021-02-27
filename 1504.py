import sys
from queue import PriorityQueue


def main():
    global N, connect
    N, E = map(int, sys.stdin.readline().split())
    connect = [[] for i in range(N + 1)]
    for i in range(E):
        s, e, d = map(int, sys.stdin.readline().split())
        connect[s].append([e, d])
        connect[e].append([s, d])
    n1, n2 = map(int, sys.stdin.readline().split())
    flag1, flag2 = 0, 0
    c1 = daik(1, n1) #1-n1으로 감
    c2 = daik(1, n2) #1-n2으로 감
    if c1 != -1:
        tmpDis = daik(n1, n2)
        if tmpDis != -1:
            c1 += tmpDis
            tmpDis = daik(n2, N)
            if tmpDis != -1:
                c1 += tmpDis
                flag1 = 1
    if c2 != -1:
        tmpDis = daik(n2, n1)
        if tmpDis != -1:
            c2 += tmpDis
            tmpDis = daik(n1, N)
            if tmpDis != -1:
                c2 += tmpDis
                flag2 = 1
    if flag1 and flag2: #둘다 1인 경우
        print(min(c1, c2))
    else:
        if flag1 == 1 and flag2 == 0:
            print(c1)
        if flag1 == 0 and flag2 == 1:
            print(c2)
        if flag1 == 0 and flag2 == 0:
            print(-1)


def daik(start, target):
    global N, connect
    visit = [-1] * (N + 1)
    q = PriorityQueue()
    visit[start] = 0
    q.put([0, start])
    while q.empty() != True:
        tmp = q.get()
        cDis, cP = tmp[0], tmp[1]
        for nxt in connect[cP]:
            nxtP, d = nxt[0], nxt[1]
            tDis = cDis + d
            if visit[nxtP] == -1:
                visit[nxtP] = tDis
                q.put([tDis, nxtP])
            else:
                if tDis < visit[nxtP]:
                    visit[nxtP] = tDis
                    q.put([tDis, nxtP])
    return visit[target]


if __name__ == '__main__':
    main()
