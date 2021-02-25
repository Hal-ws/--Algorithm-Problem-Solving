import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    dp = [[0 for j in range(M)] for i in range(N)]
    dp[0][0] = board[0][0]
    rightDir = [[0 for j in range(M)] for i in range(N)] # 우방향
    leftDir = [[0 for j in range(M)] for i in range(N)] # 좌방향
    rightDir[0][0], leftDir[0][0] = board[0][0], board[0][0]
    for j in range(1, M):
        dp[0][j] = dp[0][j - 1] + board[0][j]
        rightDir[0][j] = dp[0][j]
        leftDir[0][j] = dp[0][j]
    for i in range(1, N):
        rightDir[i][0] = dp[i - 1][0] + board[i][0]
        leftDir[i][M - 1] = dp[i - 1][M - 1] + board[i][M - 1]
        for j in range(1, M):
            rightDir[i][j] = board[i][j] + max(dp[i - 1][j], rightDir[i][j - 1])
        for j in range(M - 2, -1, -1):
            leftDir[i][j] = board[i][j] + max(dp[i - 1][j], leftDir[i][j + 1])
        for j in range(M):
            dp[i][j] = max(rightDir[i][j], leftDir[i][j])
    print(dp[N - 1][M - 1])


if __name__ == '__main__':
    main()
