import sys
from queue import PriorityQueue


def main():
    global n, connect
    T = int(sys.stdin.readline())
    for t in range(T):
        n, d, c = map(int, sys.stdin.readline().split())
        connect = [[] for i in range(n + 1)]
        for i in range(d):
            a, b, s = map(int, sys.stdin.readline().split())
            connect[b].append([a, s])
        ans = bfs(c)
        print('%s %s' %(ans[0], ans[1]))


def bfs(start):
    global n, connect
    cnt = 1
    visit = [None for j in range(n + 1)]
    q = PriorityQueue()
    visit[start] = 0
    q.put([0, start])
    maxTime = 0
    while q.empty() != True:
        tmp = q.get()
        d, c = tmp[0], tmp[1]
        for nxt in connect[c]:
            nxtP, tDis = nxt[0], d + nxt[1]
            if visit[nxtP] == None:
                cnt += 1
                visit[nxtP] = tDis
                q.put([tDis, nxtP])
            else:
                if tDis < visit[nxtP]:
                    visit[nxtP] = tDis
                    q.put([tDis, nxtP])
    for t in visit:
        if t != None and t > maxTime:
            maxTime = t
    return [cnt, maxTime]


if __name__ == '__main__':
    main()
