import sys
from queue import PriorityQueue


def main():
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    price = [[] for i in range(N + 1)]
    q = PriorityQueue()
    minPrice = [None] * (N + 1)
    for i in range(M):
        s, e, p = map(int, sys.stdin.readline().split())
        price[s].append([e, p]) #e 도시로 가는 비용 p
    start, end = map(int, sys.stdin.readline().split())
    q.put([0, start]) # 거리, 좌표
    minPrice[start] = 0
    while q.empty() == False:
        tmp = q.get()
        node, cPrice = tmp[1], tmp[0]
        linked = price[node]
        for nxt in linked:
            nxtC, tPrice = nxt[0], cPrice + nxt[1]
            if minPrice[nxtC] == None:
                minPrice[nxtC] = tPrice
                q.put([tPrice, nxtC])
            else:
                if tPrice < minPrice[nxtC]:
                    minPrice[nxtC] = tPrice
                    q.put([tPrice, nxtC])
    print(minPrice[end])


if __name__ == '__main__':
    main()

