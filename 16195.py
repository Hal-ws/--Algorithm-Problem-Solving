import sys


def main():
    dp = [[[0, 0] for j in range(1001)] for i in range(1001)] #정확하게 m개를 쓰는것, m 미만의 것을 쓰는것
    dp[1][1][0], dp[2][1][0], dp[3][1][0] = 1, 1, 1
    for i in range(1, 1001):
        for j in range(2, 1001):
            if 1 < i:
                dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j - 1][0]) % 1000000009
            if 2 < i:
                dp[i][j][0] = (dp[i][j][0] + dp[i - 2][j - 1][0]) % 1000000009
            if 3 < i:
                dp[i][j][0] = (dp[i][j][0] + dp[i - 3][j - 1][0]) % 1000000009
            dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % 1000000009
    T = int(sys.stdin.readline())
    for i in range(T):
        n, m = map(int, sys.stdin.readline().split())
        print((dp[n][m][0] + dp[n][m][1]) % 1000000009)


if __name__ == '__main__':
    main()
