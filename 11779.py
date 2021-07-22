import sys
import heapq
from math import inf


def main():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    pMatrix = [[100000 for j in range(n + 1)] for i in range(n + 1)]
    price = [[] for i in range(n + 1)]
    minPrice = [inf for i in range(n + 1)]
    minPath = ''
    hq = []
    for i in range(m):
        s, e, p = map(int, sys.stdin.readline().split())
        pMatrix[s][e] = min(pMatrix[s][e], p)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if pMatrix[i][j] != 100000:
                price[i].append([j, pMatrix[i][j]])
    start, end = map(int, sys.stdin.readline().split())
    minPrice[start] = 0
    heapq.heappush(hq, [0, start, str(start)])
    while len(hq) > 0:
        tmp = heapq.heappop(hq)
        cPrice, cPos, cPath = tmp[0], tmp[1], tmp[2]
        for nxt in price[cPos]:
            nxtP, tPrice = nxt[0], cPrice + nxt[1]
            if tPrice < minPrice[nxtP]:
                minPrice[nxtP] = tPrice
                heapq.heappush(hq, [tPrice, nxtP, cPath + ',' + str(nxtP)])
                if nxtP == end:
                    minPath = cPath + ',' + str(nxtP)
    print(minPrice[end])
    minPath = list(map(int, minPath.split(',')))
    print(len(minPath))
    for p in minPath:
        print(p, end=' ')


if __name__ == '__main__':
    main()
