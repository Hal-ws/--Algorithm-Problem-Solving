import sys
from math import inf


def main():
    N = int(sys.stdin.readline())
    matrix = []
    dp = [[0 for j in range(N)] for i in range(N)]
    size = [[[0, 0] for j in range(N)] for i in range(N)] # i부터 j까지 최소로 합쳤을때의 크기 저장
    for i in range(N):
        matrix.append(list(map(int, sys.stdin.readline().split())))
        size[i][i] = [matrix[i][0], matrix[i][1]]
    for l in range(2, N + 1): # 길이가 2부터 N까지
        for i in range(0, N + 1 - l): # 시작 idx 지정
            j = i + l - 1 # 끝 행렬 idx
            minVal = inf
            for k in range(i, j):
                tmp = dp[i][k] + dp[k + 1][j] + size[i][k][0] * size[i][k][1] * size[k + 1][j][1]
                if tmp < minVal:
                    minVal = tmp
                    size[i][j] = [size[i][k][0], size[k + 1][j][1]]
            dp[i][j] = minVal
    print(dp[0][N - 1])


if __name__ == '__main__':
    main()
