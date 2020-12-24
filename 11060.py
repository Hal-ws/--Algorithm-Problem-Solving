def main():
    N = int(input())
    board = list(map(int, input().split()))
    dp = [10000 for i in range(N)] #각 지점에 도착할 수 있는 최소 jump 수
    dp[0] = 0
    for i in range(N):
        maxJump = board[i]
        for j in range(1, maxJump + 1):
            if i + j < N:
                if dp[i] + 1 <= dp[i + j]:
                    dp[i + j] = dp[i] + 1
    if dp[N - 1] == 10000:
        print(-1)
    else:
        print(dp[N - 1])


if __name__ == '__main__':
    main()
