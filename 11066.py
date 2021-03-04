import sys
from math import inf


def main():
    T = int(sys.stdin.readline())
    for t in range(T):
        K = int(sys.stdin.readline())
        files = list(map(int, sys.stdin.readline().split()))
        dp = [[0 for j in range(K)] for i in range(K)]
        for l in range(1, K + 1): # 길이가 2개부터 K까지
            for i in range(K - l + 1):
                j = i + l - 1 # i부터 j까지 합의 최소값 구함
                if i == j:
                    dp[i][j] = files[i]
                elif j == i + 1:
                    dp[i][j] = files[i] + files[j]
                else:
                    minV = inf
                    for d in range(i, j): #i 부터 j 사이에 자름
                        tmp = (dp[i][d] + dp[d + 1][j]) * 2
                        if tmp < minV:
                            minV = tmp
                    dp[i][j] = minV
        for i in range(K):
            print(dp[i])
        print(dp[0][K - 1])


if __name__ == '__main__':
    main()
