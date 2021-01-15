import sys


def main():
    T = int(sys.stdin.readline())
    dp = [[[0, 0] for j in range(101)] for i in range(101)]
    dp[1][0][0] = 1
    dp[1][0][1] = 1
    for i in range(2, 101):
        for j in range(101):
            if j == 0:
                dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][1]
                dp[i][j][1] = dp[i - 1][j][0]
            else:
                dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][1]
                dp[i][j][1] = dp[i - 1][j - 1][1] + dp[i - 1][j][0]

    for i in range(T):
        n, k = map(int, sys.stdin.readline().split())
        print(sum(dp[n][k]))


if __name__ == '__main__':
    main()
