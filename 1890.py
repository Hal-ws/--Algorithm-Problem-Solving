import sys


def main():
    N = int(sys.stdin.readline())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    dp = [[0 for i in range(N)] for j in range(N)]
    visited = [[0 for i in range(N)] for j in range(N)]
    visited[0][0] = 1
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            if i == N - 1 and j == N - 1:
                break
            if visited[i][j] == 1 and board[i][j] != 0 and i + board[i][j] <= N - 1:
                stopflag = 1
                for k in range(i + 1, i + board[i][j]):
                    if board[k][j] == 0:
                        stopflag = 0
                        break
                if stopflag:
                    dp[i + board[i][j]][j] += dp[i][j]
                    visited[i + board[i][j]][j] = 1
            if visited[i][j] == 1 and board[i][j] != 0 and j + board[i][j] <= N - 1:
                stopflag = 1
                for k in range(j + 1, j + board[i][j]):
                    if board[i][k] == 0:
                        stopflag = 0
                        break
                if stopflag:
                    dp[i][j + board[i][j]] += dp[i][j]
                    visited[i][j + board[i][j]] = 1
    print(dp[N - 1][N - 1])


if __name__ == "__main__":
    main()
