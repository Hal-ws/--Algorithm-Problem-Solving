def main():
    N = int(input())
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(2, N + 1, 2):
        dp[i] += dp[i - 2] * 3
        for j in range(4, N + 1, 2): #추가할 수 있는 block의 사이즈
            if i - j >= 0:
                dp[i] += dp[i - j] * 2
    print(dp[N])


if __name__ == "__main__":
    main()
