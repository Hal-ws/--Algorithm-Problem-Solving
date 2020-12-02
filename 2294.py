import sys


def main():
    N, K = map(int, sys.stdin.readline().split())
    coins = [0] * (N + 1)
    for i in range(N):
        coins[i] = int(sys.stdin.readline())
    dp = [0] * (K + 1)
    dp[0] = 0
    for j in range(1, K + 1):
        minSize = 10001
        for i in range(N):
            if j - coins[i] >= 0:
                if dp[j - coins[i]] + 1 <= minSize:
                    minSize = dp[j - coins[i]] + 1
        dp[j] = minSize
    if dp[K] != 10001:
        print(dp[K])
    else:
        print(-1)


if __name__ == "__main__":
    main()
