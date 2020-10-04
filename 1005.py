import sys


def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        N, K = map(int, sys.stdin.readline().split())
        buildtime = list(map(int, sys.stdin.readline().split()))
        buildorder = [[[None], [None]] for i in range(N + 1)]
        startbuilding = []
        for j in range(K):
            X, Y = map(int, sys.stdin.readline().split())
            if buildorder[Y][0][0] == None:
                buildorder[Y][0][0] = X
            else:
                buildorder[Y][0].append(X)
            if buildorder[X][1][0] == None:
                buildorder[X][1][0] = Y
            else:
                buildorder[X][1].append(Y)
        for j in range(1, N + 1):
            if buildorder[j][0] == [None]:
                startbuilding.append(j)
        W = int(sys.stdin.readline())
        print(buildorder)
        print(startbuilding)




if __name__ == "__main__":
    main()

