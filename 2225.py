def main():
    N, K = map(int, input().split())
    dp = [[0 for i in range(N + 1)] for j in range(K + 1)]
    for i in range(1, N + 1):
        dp[1][i] = 1
    for i in range(1, K + 1):
        dp[i][1] = i
    for i in range(2, K + 1):
        for j in range(2, N + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp[K][N] % 1000000000)


if __name__ == "__main__":
    main()
