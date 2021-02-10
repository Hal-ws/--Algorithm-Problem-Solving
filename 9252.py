def main():
    a = ' ' + input()
    b = ' ' + input()
    al, bl = len(a), len(b)
    dp = [[[0, ''] for j in range(al)] for i in range(bl)]
    for i in range(1, bl):
        for j in range(1, al):
            if b[i] == a[j]:
                dp[i][j][0] = dp[i - 1][j - 1][0] + 1
                dp[i][j][1] = dp[i - 1][j - 1][1] + b[i]
            else:
                if dp[i - 1][j][0] < dp[i][j - 1][0]:
                    dp[i][j][0], dp[i][j][1] = dp[i][j - 1][0], dp[i][j - 1][1]
                else:
                    dp[i][j][0], dp[i][j][1] = dp[i - 1][j][0], dp[i - 1][j][1]
    print(dp[bl - 1][al - 1][0])
    print(dp[bl - 1][al - 1][1])


if __name__ == '__main__':
    main()
