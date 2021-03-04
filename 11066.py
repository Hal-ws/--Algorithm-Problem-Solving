import sys
from math import inf


def main():
    T = int(sys.stdin.readline())
    for t in range(T):
        K = int(sys.stdin.readline())
        files = list(map(int, sys.stdin.readline().split()))
        dp = [[[0, 0] for j in range(K)] for i in range(K)] # 합, 누적 비용
        for l in range(1, K + 1): # 길이가 2개부터 K까지
            for i in range(K - l + 1):
                j = i + l - 1 # i부터 j까지 합의 최소값 구함
                if i == j:
                    dp[i][j][0], dp[i][j][1] = files[i], 0
                elif j == i + 1:
                    dp[i][j][0], dp[i][j][1] = files[i] + files[j], files[i] + files[j]
                else:
                    minSum = inf
                    minCost = inf
                    for d in range(i, j): #i 부터 j 사이에 자름
                        fileSum = dp[i][d][0] + dp[d + 1][j][0]
                        costSum = dp[i][d][1] + dp[d + 1][j][1] + fileSum
                        if costSum < minCost:
                            minSum = fileSum
                            minCost = costSum
                    dp[i][j] = [minSum, minCost]
        print(dp[0][K - 1][1])


if __name__ == '__main__':
    main()
