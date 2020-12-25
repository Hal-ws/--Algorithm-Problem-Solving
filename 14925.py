import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    dp = [[[0, 0, 0] for j in range(M)] for i in range(N)] #제일 긴 세로선, 가로선, 정사각형 사이즈
    maxSize = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                if i == 0 and j == 0:
                    dp[i][j][0] = 1
                    dp[i][j][1] = 1
                    dp[i][j][2] = 1
                elif i == 0:
                    dp[i][j][0] = 1
                    dp[i][j][1] = dp[i][j - 1][0] + 1
                    dp[i][j][2] = 1
                elif j == 0:
                    dp[i][j][0] = dp[i - 1][j][0] + 1
                    dp[i][j][1] = 1
                    dp[i][j][2] = 1
                else:
                    dp[i][j][0] = dp[i - 1][j][0] + 1
                    dp[i][j][1] = dp[i][j - 1][1] + 1
                    dp[i][j][2] = min(dp[i - 1][j][0], dp[i][j - 1][1], dp[i - 1][j - 1][2]) + 1
                if maxSize <= dp[i][j][2]:
                    maxSize = dp[i][j][2]
    print(maxSize)


if __name__ == '__main__':
    main()
