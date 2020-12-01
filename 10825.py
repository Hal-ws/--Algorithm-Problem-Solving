def main():
    N = int(input())
    inputList = list(map(int, input().split()))
    process = inputList[:N - 1]
    result = inputList[N - 1]
    dp = [[0 for i in range(21)] for j in range(N - 1)]
    dp[0][process[0]] = 1
    for i in range(1, N - 1):
        val = process[i]
        for j in range(21):
            if dp[i - 1][j] != 0 and j - val >= 0:
                dp[i][j - val] += dp[i - 1][j]
            if dp[i - 1][j] != 0 and j + val < 21:
                dp[i][j + val] += dp[i - 1][j]
    print(dp[N - 2][result])


if __name__ == "__main__":
    main()
