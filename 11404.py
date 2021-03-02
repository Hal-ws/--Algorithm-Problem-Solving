import sys
from math import inf


def main():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    disMatrix = [[inf for j in range(n + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        disMatrix[i][i] = 0
    for i in range(m):
        s, e, d = map(int, sys.stdin.readline().split())
        if d < disMatrix[s][e]:
            disMatrix[s][e] = d
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if disMatrix[i][k] + disMatrix[k][j] < disMatrix[i][j]:
                    disMatrix[i][j] = disMatrix[i][k] + disMatrix[k][j]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if disMatrix[i][j] == inf:
                disMatrix[i][j] = 0
            print(disMatrix[i][j], end=' ')
        print()


if __name__ == '__main__':
    main()
