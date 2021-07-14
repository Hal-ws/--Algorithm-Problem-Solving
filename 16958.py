import sys
from math import inf


def main():
    N, T = map(int, sys.stdin.readline().split())
    cityInfo = [[] for i in range(N + 1)]
    disMatrix = [[inf for j in range(N + 1)] for i in range(N + 1)]
    for i in range(1, N + 1):
        disMatrix[i][i] = 0
        cityInfo[i] = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            city1, city2 = cityInfo[i], cityInfo[j]
            dis1 = abs(city1[1] - city2[1]) + abs(city1[2] - city2[2])
            if dis1 < disMatrix[i][j]:
                disMatrix[i][j] = dis1
            if dis1 < disMatrix[j][i]:
                disMatrix[j][i] = dis1
            if city1[0] == city2[0] == 1:
                if T < disMatrix[i][j]:
                    disMatrix[i][j] = T
                if T < disMatrix[j][i]:
                    disMatrix[j][i] = T
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if disMatrix[i][k] + disMatrix[k][j] < disMatrix[i][j]:
                    disMatrix[i][j] = disMatrix[i][k] + disMatrix[k][j]
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        print(disMatrix[a][b])


if __name__ == '__main__':
    main()
