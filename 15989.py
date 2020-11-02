def main():
    dp = [[0, 0, 1], [0, 1, 1], [1, 1, 1]]
    for i in range(3, 10000):
        dp.append([sum(dp[i - 3]), dp[i - 2][1] + dp[i - 2][2], 1])
    T = int(input())
    for i in range(T):
        print(sum(dp[int(input()) - 1]))


if __name__ == "__main__":
    main()
