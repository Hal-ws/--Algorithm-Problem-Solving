import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    dp = [[0 for j in range(N)] for i in range(N)]
    dp[0][0] = board[0][0]
    for j in range(1, N):
        dp[0][j] = dp[0][j - 1] + board[0][j]
    for i in range(1, N):
        dp[i][0] = dp[i - 1][0] + board[i][0]
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + board[i][j]
    for i in range(M):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        if x1 >= 1 and y1 >= 1:
            print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])
        elif x1 == 0 and y1 >= 1:
            print(dp[x2][y2] - dp[x2][y1 - 1])
        elif x1 >= 1 and y1 == 0:
            print(dp[x2][y2] - dp[x1 - 1][y2])
        else:
            print(dp[x2][y2])


if __name__ == '__main__':
    main()
