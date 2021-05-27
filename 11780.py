import sys
from copy import deepcopy


def main():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    inf = 100000 * 100000 + 1
    disMatrix = [[inf for j in range(n)] for i in range(n)]
    pathMatrix = [[[] for j in range(n)] for i in range(n)]
    for i in range(n):
        pathMatrix[i][i].append(i)
        disMatrix[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        a, b = a - 1, b - 1
        if c < disMatrix[a][b]:
            disMatrix[a][b] = c
            pathMatrix[a][b] = [a, b]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                tmpDis = disMatrix[i][k] + disMatrix[k][j]
                if tmpDis < disMatrix[i][j]:
                    path1, path2 = pathMatrix[i][k], pathMatrix[k][j]
                    if path1[-1] == k:
                        nPath1 = deepcopy(path1[:len(path1) - 1])
                    if path2[0] == k:
                        nPath2 = deepcopy(path2[1:])
                    disMatrix[i][j] = tmpDis
                    pathMatrix[i][j] = nPath1 + [k] + nPath2
    for i in range(n):
        for j in range(n):
            if disMatrix[i][j] == inf:
                print(0, end=' ')
            else:
                print(disMatrix[i][j], end=' ')
        print()
    for i in range(n):
        for j in range(n):
            if len(pathMatrix[i][j]) == 1:
                print(0)
            else:
                print(len(pathMatrix[i][j]), end=' ')
                for p in pathMatrix[i][j]:
                    print(p + 1, end=' ')
                print()


if __name__ == '__main__':
    main()
