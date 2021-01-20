import sys
from queue import PriorityQueue


def main():
    V, E = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())
    q = PriorityQueue()
    dis = [[] for i in range(V + 1)]
    minDis = [None] * (V + 1)
    minDis[K] = 0
    q.put([0, K]) #거리, node 집어넣음
    for i in range(E):
        s, e, d = map(int, sys.stdin.readline().split())
        dis[s].append([e, d])
    while q.empty() != True:
        tmp = q.get()
        node, cDis = tmp[1], tmp[0]
        linked = dis[node]
        for nxt in linked:
            if minDis[nxt[0]] == None:
                minDis[nxt[0]] = cDis + nxt[1]
                q.put([cDis + nxt[1], nxt[0]])
            else:
                if cDis + nxt[1] < minDis[nxt[0]]:
                    q.put([cDis + nxt[1], nxt[0]])
                    minDis[nxt[0]] = cDis + nxt[1]
    for i in range(1, V + 1):
        if minDis[i] == None:
            print('INF')
        else:
            print(minDis[i])


if __name__ == '__main__':
    main()
