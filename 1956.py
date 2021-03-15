import sys


def main():
    V, E = map(int, sys.stdin.readline().split())
    inf = 4 * pow(10, 6) + 1
    ans = inf
    disMatrix = [[inf for j in range(V)] for i in range(V)]
    for i in range(E):
        start, end, dis = map(int, sys.stdin.readline().split())
        disMatrix[start - 1][end - 1] = dis
    for k in range(V):
        for i in range(V):
            for j in range(V):
                tmpDis = disMatrix[i][k] + disMatrix[k][j]
                if tmpDis < disMatrix[i][j]:
                    disMatrix[i][j] = tmpDis
    for i in range(V):
        if disMatrix[i][i] < ans:
            ans = disMatrix[i][i]
    if ans == inf:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
