def main():
    N = int(input())
    house = []
    for i in range(N):
        house.append(list(map(int, input().split())))
    dp = [[[0, 0, 0] for i in range(N)] for j in range(N)]
    state = [[[0, 0, 0] for i in range(N)] for j in range(N)]
    state[0][1][0] = "l" # l(linear), v(vertical), d(diagonal)
    for i in range(N):
        for j in range(N):
            if i == 0 and (j == 0 or j == 1):
                dp[i][j][0] = 1
            if state[i][j][0] == "l":
                if j + 1 < N and house[i][j + 1] == 0:
                    dp[i][j + 1][0] += dp[i][j][0]
                    state[i][j + 1][0] = "l"
                if i + 1 < N and j + 1 < N and house[i + 1][j] == 0 and house[i][j + 1] == 0 and house[i + 1][j + 1] == 0:
                    dp[i + 1][j + 1][2] += dp[i][j][0]
                    state[i + 1][j + 1][2] = "d"
            if state[i][j][1] == "v":
                if i + 1 < N and house[i + 1][j] == 0:
                    dp[i + 1][j][1] += dp[i][j][1]
                    state[i + 1][j][1] = "v"
                if i + 1 < N and j + 1 < N and house[i + 1][j] == 0 and house[i][j + 1] == 0 and house[i + 1][
                    j + 1] == 0:
                    dp[i + 1][j + 1][2] += dp[i][j][1]
                    state[i + 1][j + 1][2] = "d"
            if state[i][j][2] == "d":
                if i + 1 < N and house[i + 1][j] == 0:
                    dp[i + 1][j][1] += dp[i][j][2]
                    state[i + 1][j][1] = "v"
                if j + 1 < N and house[i][j + 1] == 0:
                    dp[i][j + 1][0] += dp[i][j][2]
                    state[i][j + 1][0] = "l"
                if i + 1 < N and j + 1 < N and house[i + 1][j] == 0 and house[i][j + 1] == 0 and house[i + 1][
                    j + 1] == 0:
                    dp[i + 1][j + 1][2] += dp[i][j][2]
                    state[i + 1][j + 1][2] = "d"
    print(sum(dp[N - 1][N - 1]))


if __name__ == "__main__":
    main()
