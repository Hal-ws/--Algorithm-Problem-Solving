import sys
import heapq
from math import inf, sqrt


def main():
    N, W = map(int, sys.stdin.readline().split())
    M = float(sys.stdin.readline())
    lineLengths = [inf for i in range(N + 1)]
    posXY = [[] for i in range(N + 1)]
    alrdyConnect = [[0 for j in range(N + 1)] for i in range(N + 1)]
    for i in range(N):
        posXY[i + 1] = list(map(int, sys.stdin.readline().split()))
    for i in range(W):
        a, b = map(int, sys.stdin.readline().split())
        alrdyConnect[a][b] = 1
        alrdyConnect[b][a] = 1
    hq = []
    heapq.heappush(hq, [0, 1]) # 거리, 위치 저장
    lineLengths[1] = 0
    while len(hq) > 0:
        tmp = heapq.heappop(hq)
        cDis, pos = tmp[0], tmp[1]
        for nxtPos in range(1, N + 1): # 다음 좌표
            if alrdyConnect[pos][nxtPos] and cDis < lineLengths[nxtPos]: # 이미 연결돼있으니 무료로 갈수있음
                lineLengths[nxtPos] = cDis
                heapq.heappush(hq, [cDis, nxtPos])
            else:
                x1, y1 = posXY[pos][0], posXY[pos][1]
                x2, y2 = posXY[nxtPos][0], posXY[nxtPos][1]
                if pow(x2 - x1, 2) + pow(y2 - y1, 2) <= pow(M, 2): # 거리 도달가능
                    tDis = cDis + sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
                    if tDis < lineLengths[nxtPos]:
                        lineLengths[nxtPos] = tDis
                        heapq.heappush(hq, [tDis, nxtPos])
    print(int(lineLengths[N] * 1000))


if __name__ == "__main__":
    main()
