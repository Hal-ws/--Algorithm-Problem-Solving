import sys


def main():
    dp = [[0 for i in range(31)] for j in range(61)]
    for i in range(1, 61):
        dp[i][0] = 1
    for j in range(1, 31):
        for i in range(61 - 2 * j):
            if j > 0: #1개짜리가 1개 이상 있을때
                dp[i][j] += dp[i + 1][j - 1]
            if i > 0: #반개짜리가 1개 이상 있을때
                dp[i][j] += dp[i - 1][j]
    while 1:
        N = int(sys.stdin.readline())
        if N == 0:
            break
        print(dp[0][N])


if __name__ == "__main__":
    main()
