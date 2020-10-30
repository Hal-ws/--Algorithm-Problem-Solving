def main():
    N = int(input())
    dp = [0] * (N + 1)
    dp[0] = 0
    dp[1] = 3
    if N > 1:
        dp[2] = 7
    for i in range(3, N + 1):
        dp[i] = (dp[i - 2] + 2 * dp[i - 1]) % 9901
    print(dp[N])


if __name__ == "__main__":
    main()
