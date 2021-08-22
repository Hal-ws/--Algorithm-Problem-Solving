import sys
import heapq
from math import inf


def main():
    N, M, K = map(int, sys.stdin.readline().split())
    connect = [[] for i in range(N + 1)]
    dp = [[inf for j in range(N + 1)] for i in range(K + 1)]
    dp[0][1] = 0 # 0개의 경로를 없애고 1에 도착할때 드는 비용은 0
    for i in range(M):
        a, b, cost = map(int, sys.stdin.readline().split())
        connect[a].append([b, cost])
        connect[b].append([a, cost])
    hq = []


if __name__ == "__main__":
    main()
