import sys
import heapq
from math import inf


def main():
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    pMatrix = [[100000 for j in range(N + 1)] for i in range(N + 1)]
    price = [[] for i in range(N + 1)]
    q = []
    minPrice = [inf] * (N + 1)
    for i in range(M):
        s, e, p = map(int, sys.stdin.readline().split())
        if p < pMatrix[s][e]:
            pMatrix[s][e] = p
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if pMatrix[i][j] != 100000:
                price[i].append([j, pMatrix[i][j]])
    start, end = map(int, sys.stdin.readline().split())
    minPrice[start] = 0
    heapq.heappush(q, [0, start])
    minPrice[start] = 0
    while len(q) > 0:
        tmp = heapq.heappop(q)
        cPrice, cPos = tmp[0], tmp[1]
        for nxt in price[cPos]:
            nxtP, sumPrice = nxt[0], cPrice + nxt[1]
            if sumPrice < minPrice[nxtP]:
                minPrice[nxtP] = sumPrice
                heapq.heappush(q, [sumPrice, nxtP])
    print(minPrice[end])


if __name__ == '__main__':
    main()
