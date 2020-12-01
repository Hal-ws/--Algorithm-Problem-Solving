def main():
    N, S, M = map(int, input().split())
    V = list(map(int, input().split()))
    dp = [[0 for i in range(M + 1)] for j in range(N + 1)]
    if S - V[0] >= 0:
        dp[1][S - V[0]] = 1
    if S + V[0] <= M:
        dp[1][S + V[0]] = 1
    for i in range(1, N):
        for j in range(M + 1):
            if dp[i][j]:
                if j - V[i] >= 0:
                    dp[i + 1][j - V[i]] = 1
                if j + V[i] <= M:
                    dp[i + 1][j + V[i]] = 1
    flag = 0
    for j in range(M, -1, -1):
        if dp[N][j]:
            ans = j
            flag = 1
            break
    if flag:
        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()
