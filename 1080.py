import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    start, target = [], []
    diffMatrix = [[0 for j in range(M)] for i in range(N)]
    for i in range(N):
        start.append(list(map(int, list(sys.stdin.readline()[:M]))))
    for i in range(N):
        target.append(list(map(int, list(sys.stdin.readline()[:M]))))
    ans = 0
    for i in range(N):
        for j in range(M):
            diffMatrix[i][j] = start[i][j] != target[i][j]
    if start == target:
        print(ans)
        return
    if N < 3 or M < 3:
        print(-1)
        return
    for i in range(N - 2):
        for j in range(M - 2):
            if diffMatrix[i][j] == True:
                reversing(i, j, diffMatrix)
                ans += 1
            if finishChk(diffMatrix, N, M):
                print(ans)
                return
    print(-1)
    return


def reversing(y, x, diffMatrix):
    for i in range(y, y + 3):
        for j in range(x, x + 3):
            if diffMatrix[i][j] == True:
                diffMatrix[i][j] = False
            else:
                diffMatrix[i][j] = True


def finishChk(diffMatrix, N, M):
    for i in range(N):
        for j in range(M):
            if diffMatrix[i][j]:  # True가 하나라도 있으면 끝난게 아님
                return 0
    return 1
    

if __name__ == '__main__':
    main()
