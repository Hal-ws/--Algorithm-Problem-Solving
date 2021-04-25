import sys
from math import inf


def main():
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    disMatrix = [[inf for j in range(N)] for i in range(N)]
    pathMatrix = [[[] for j in range(N)] for i in range(N)]
    for i in range(N):
        disMatrix[i][i] = 0
        for j in range(N):
            pathMatrix[i][j].append(i)
    for i in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        a, b = a - 1, b - 1
        if c < disMatrix[a][b]:
            disMatrix[a][b] = c
            pathMatrix[a][b] = [a, b]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if disMatrix[i][k] + disMatrix[k][j] < disMatrix[i][j]:
                    tmp = []
                    for l in range(len(pathMatrix[i][k]) - 1):
                        tmp.append(pathMatrix[i][k][l])
                    for l in range(len(pathMatrix[k][j])):
                        tmp.append(pathMatrix[k][j][l])
                    disMatrix[i][j] = disMatrix[i][k] + disMatrix[k][j]
                    pathMatrix[i][j] = tmp
    for i in range(N):
        for j in range(N):
            print(disMatrix[i][j], end=' ')
        print()
    for i in range(N):
        for j in range(N):
            l = len(pathMatrix[i][j])
            if l == 1:
                print(0)
            else:
                print(l, end=' ')
                for p in pathMatrix[i][j]:
                    print(p + 1, end=' ')
                print()


if __name__ == '__main__':
    main()
