import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    paper = []
    for i in range(N):
        paper.append(list(map(int, sys.stdin.readline().split())))
    #bar
    max1 = 0
    for i in range(N):
        for j in range(M - 3):
            temp = paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i][j + 3]
            max1 = max(temp, max1)
    for i in range(N - 3):
        for j in range(M):
            temp = paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i + 3][j]
            max1 = max(temp, max1)
    #box
    max2 = 0
    for i in range(N - 1):
        for j in range(M - 1):
            temp = paper[i][j] + paper[i + 1][j] + paper[i][j + 1] + paper[i + 1][j + 1]
            max2 = max(temp, max2)
    # 꺾인 bar
    max3 = 0
    for i in range(N - 2):
        for j in range(M - 1):
            temp = paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i + 2][j + 1]
            max3 = max(max3, temp)
    for i in range(N - 1):
        for j in range(M - 2):
            temp = paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i + 1][j]
            max3 = max(max3, temp)
    for i in range(N - 2):
        for j in range(M - 1):
            temp = paper[i][j] + paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 2][j + 1]
            max3 = max(max3, temp)
    for i in range(N - 1):
        for j in range(M - 2):
            temp = paper[i][j + 2] + paper[i + 1][j + 2] + paper[i + 1][j + 1] + paper[i + 1][j]
            max3 = max(max3, temp)
    for i in range(N - 2):
        for j in range(M - 1):
            temp = paper[i + 2][j] + paper[i + 2][j + 1] + paper[i + 1][j + 1] + paper[i][j + 1]
            max3 = max(max3, temp)
    for i in range(N - 1):
        for j in range(M - 2):
            temp = paper[i][j] + paper[i + 1][j] + paper[i + 1][j + 1] + paper[i + 1][j + 2]
            max3 = max(max3, temp)
    for i in range(N - 2):
        for j in range(M - 1):
            temp = paper[i][j + 1] + paper[i][j] + paper[i + 1][j] + paper[i + 2][j]
            max3 = max(max3, temp)
    for i in range(N - 1):
        for j in range(M - 2):
            temp = paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i + 1][j + 2]
            max3 = max(max3, temp)
    # 두번꺾임
    max4 = 0
    for i in range(N - 2):
        for j in range(M - 1):
            temp = paper[i][j] + paper[i + 1][j] + paper[i + 1][j + 1] + paper[i + 2][j + 1]
            max4 = max(max4, temp)
    for i in range(N - 1):
        for j in range(M - 2):
            temp = paper[i + 1][j] + paper[i + 1][j + 1] + paper[i][j + 1] + paper[i][j + 2]
            max4 = max(max4, temp)
    for i in range(N - 2):
        for j in range(M - 1):
            temp = paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 1][j] + paper[i + 2][j]
            max4 = max(max4, temp)
    for i in range(N - 1):
        for j in range(M - 2):
            temp = paper[i][j] + paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 1][j + 2]
            max4 = max(max4, temp)
    # 마지막
    max5 = 0
    for i in range(N - 1):
        for j in range(M - 2):
            temp = paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 1][j] + paper[i + 1][j + 2]
            max5 = max(max5, temp)
    for i in range(N - 1):
        for j in range(M - 2):
            temp = paper[i][j] + paper[i][j + 1] + paper[i + 1][j + 1] + paper[i][j + 2]
            max5 = max(max5, temp)
    for i in range(N - 2):
        for j in range(M - 1):
            temp = paper[i][j] + paper[i + 1][j] + paper[i + 1][j + 1] + paper[i + 2][j]
            max5 = max(max5, temp)
    for i in range(N - 2):
        for j in range(M - 1):
            temp = paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 1][j] + paper[i + 2][j + 1]
            max5 = max(max5, temp)
    print(max(max1, max2, max3, max4, max5))


if __name__ == "__main__":
    main()

