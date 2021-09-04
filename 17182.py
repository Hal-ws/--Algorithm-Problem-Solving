import sys
from itertools import permutations


def main():
    N, K = map(int, sys.stdin.readline().split())
    tMatrix = []
    for i in range(N):
        tMatrix.append(list(map(int, sys.stdin.readline().split())))
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if tMatrix[i][k] + tMatrix[k][j] < tMatrix[i][j]:
                    tMatrix[i][j] = tMatrix[i][k] + tMatrix[k][j]
    pathNodes = []
    for i in range(N):
        if i != K:
            pathNodes.append(i)
    paths = list(permutations(pathNodes, len(pathNodes)))
    ans = None
    for path in paths:
        for i in range(len(path)):
            if i == 0:
                culDis = tMatrix[K][path[i]]
            else:
                culDis += tMatrix[path[i - 1]][path[i]]
        if ans == None or culDis < ans:
            ans = culDis
    print(ans)


if __name__ == "__main__":
    main()
