import sys
import heapq
from math import inf


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M, K = map(int, sys.stdin.readline().split())
        connect = [[] for i in range(N + 1)]
        for i in range(K):
            u, v, c, d = map(int, sys.stdin.readline().split())
            connect[u].append([v, c, d])
        print(daikstra(connect, N, M))
    return 0


def daikstra(connect, N, M):
    dp = [[inf for j in range(M + 1)] for i in range(N + 1)]
    for j in range(1, M + 1):
        dp[1][j] = 0 # 1까지 j원을 들여서 갈 수 있는 시간은 최소 0
    hq = []
    heapq.heappush(hq, [0, 0, 1]) # 시간, 비용, 위치
    while len(hq) > 0:
        tmp = heapq.heappop(hq)
        usedT, cost, pos = tmp[0], tmp[1], tmp[2]
        for nxt in connect[pos]: # 연결된 다른 지점 확인
            nxtP, addC, addT = nxt[0], nxt[1], nxt[2]
            if cost + addC <= M: # M원보다 작아야함
                if usedT + addT < dp[nxtP][cost + addC]:
                    dp[nxtP][cost + addC] = usedT + addT
                    for i in range(cost + addC + 1, M + 1):
                        if dp[nxtP][i] > usedT + addT:
                            dp[nxtP][i] = usedT + addT
                        else:
                            break
                    heapq.heappush(hq, [usedT + addT, cost + addC, nxtP])
    answer = min(dp[N])
    if answer < 1000 * 10000 + 1:
        return answer
    return "Poor KCM"


if __name__ == '__main__':
    main()
