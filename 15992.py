import sys


def main():
    T = int(sys.stdin.readline())
    dp = [[0 for j in range(1001)] for i in range(1001)]
    dp[1][1], dp[1][2], dp[1][3] = 1, 1, 1
    for i in range(2, 1001):
        for j in range(1001):
            if j - 1 >= 0:
                dp[i][j] += dp[i - 1][j - 1] % 1000000009
            if j - 2 >= 0:
                dp[i][j] += dp[i - 1][j - 2] % 1000000009
            if j - 3 >= 0:
                dp[i][j] += dp[i - 1][j - 3] % 1000000009
            dp[i][j] = dp[i][j] % 1000000009
    for i in range(T):
        n, m = map(int, sys.stdin.readline().split())
        print(dp[m][n])


if __name__ == '__main__':
    main()
