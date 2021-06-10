import sys
from collections import deque


def main():
    N, P, K = map(int, sys.stdin.readline().split())
    connect = [[] for i in range(N + 1)]
    for _ in range(P):
        c1, c2, Price = map(int, sys.stdin.readline().split())
        connect[c1].append([c2, Price])
        connect[c2].append([c1, Price])
    answer = 1000001
    left, right = 0, 1000000
    while left <= right:
        mid = (left + right) // 2
        chk = chkPossible(mid, K, connect, N)
        if chk:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    if answer == 1000001:
        answer = -1
    print(answer)


def chkPossible(maxP, K, connnect, N):
    visit = [[0 for j in range(N + 1)] for i in range(K + 1)]
    q = deque()
    q.append([1, K])
    visit[K][1] = 1
    while len(q) > 0:
        tmp = q.popleft()
        curP, leftK = tmp[0], tmp[1]
        for nxt in connnect[curP]:
            nxtP, price = nxt[0], nxt[1]
            if price > maxP:
                if leftK >= 1 and visit[leftK - 1][nxtP] == 0:
                    visit[leftK - 1][nxtP] = 1
                    q.append([nxtP, leftK - 1])
                    if nxtP == N:
                        return 1
            else:
                if visit[leftK][nxtP] == 0:
                    visit[leftK][nxtP] = 1
                    q.append([nxtP, leftK])
                    if nxtP == N:
                        return 1
    return 0


if __name__ == '__main__':
    main()
