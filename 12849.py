def main():
    D = int(input())
    dp = [[0 for j in range(8)] for i in range(D + 1)]
    dp[1][1], dp[1][2] = 1, 1
    for i in range(2, D + 1):
        dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 1000000007
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][2] + dp[i - 1][3]) % 1000000007
        dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][4]) % 1000000007
        dp[i][3] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4] + dp[i - 1][5]) % 1000000007
        dp[i][4] = (dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][5] + dp[i - 1][7]) % 1000000007
        dp[i][5] = (dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][6]) % 1000000007
        dp[i][6] = (dp[i - 1][5] + dp[i - 1][7]) % 1000000007
        dp[i][7] = (dp[i - 1][4] + dp[i - 1][6]) % 1000000007
    print(dp[D][0])


if __name__ == '__main__':
    main()
