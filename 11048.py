import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    miro =[]
    for i in range(N):
        miro.append(list(map(int, sys.stdin.readline().split())))
    dp = [[0 for i in range(M)] for j in range(N)]
    dp[0][0] = miro[0][0]
    for i in range(N):
        for j in range(M):
            if i == 0 and j == 0:
                continue
            elif i == 0 and j != 0:
                dp[i][j] = miro[i][j] + dp[i][j - 1]
            elif i != 0 and j == 0:
                dp[i][j] = miro[i][j] + dp[i - 1][j]
            else:
                dp[i][j] = miro[i][j] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    print(dp[N - 1][M - 1])


if __name__ == "__main__":
    main()
