import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline()[:M])))
    dp = [[0 for i in range(M)] for j in range(N)]
    maxLen = 0
    for i in range(N):
        for j in range(M):
            if i == 0:
                if board[i][j]:
                    dp[i][j] = 1
            if j == 0:
                if board[i][j]:
                    dp[i][j] = 1
            if i > 0 and j > 0:
                if board[i][j] and board[i - 1][j] and board[i][j - 1]:
                    if dp[i - 1][j] == dp[i][j - 1]:
                        d = dp[i - 1][j]
                        if board[i - d][j - d] == 1:
                            dp[i][j] = d + 1
                        else:
                            dp[i][j] = d
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                elif board[i][j]:
                    dp[i][j] = 1
            if dp[i][j] >= maxLen:
                maxLen = dp[i][j]
    print(maxLen * maxLen)


if __name__ == "__main__":
    main()
