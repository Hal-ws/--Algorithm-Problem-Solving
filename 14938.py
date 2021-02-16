import sys
from queue import PriorityQueue


def main():
    global n, m, r, dMatrix, items, connect
    n, m, r = map(int, sys.stdin.readline().split())
    dMatrix = [[-1 for j in range(n + 1)] for i in range(n + 1)]
    connect = [[] for i in range(n + 1)]
    items = [None] + list(map(int, sys.stdin.readline().split()))
    for i in range(r):
        a, b, l = map(int, sys.stdin.readline().split())
        connect[a].append([b, l])
        connect[b].append([a, l])
    for point in range(1, n + 1):
        getDis(point) # 1~n 포인트별로 다른 포인트까지 가는 최소거리 구함
    ans = 0
    for i in range(1, n + 1):
        tmp = 0
        for j in range(1, n + 1):
            if dMatrix[i][j] <= m and dMatrix[i][j] != -1:
                tmp += items[j]
        if ans < tmp:
            ans = tmp
    print(ans)


def getDis(start):
    global n, m, r, dMatrix, items, connect
    q = PriorityQueue()
    q.put([0, start])
    dMatrix[start][start] = 0
    while q.empty() != True:
        tmp = q.get()
        cur, dis = tmp[1], tmp[0]
        for nxt in connect[cur]:
            nP = nxt[0]
            disToNxt = nxt[1]
            if dMatrix[start][nP] == -1:
                dMatrix[start][nP] = dis + disToNxt
                q.put([dis + disToNxt, nP])
            elif dis + disToNxt < dMatrix[start][nP]:
                dMatrix[start][nP] = dis + disToNxt
                q.put([dis + disToNxt, nP])


if __name__ == '__main__':
    main()
