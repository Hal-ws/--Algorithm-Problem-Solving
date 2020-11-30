import sys


def main():
    N, K = map(int, sys.stdin.readline().split())
    coins = [0] * N
    for i in range(N):
        coins[i] = int(sys.stdin.readline())
    dp = [0] * (K + 1)
    dp[0] = 1
    for i in coins:
        for j in range(1, K + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]
    print(dp[K])


if __name__ == "__main__":
    main()
