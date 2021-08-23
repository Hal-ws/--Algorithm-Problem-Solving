import sys


def main():
    N, M, K = map(int, sys.stdin.readline().split())
    board = []
    answer = 0
    for i in range(N):
        board.append(sys.stdin.readline()[:M])
    target = sys.stdin.readline()
    target = target[:len(target) - 1]
    dp = [[[-1 for j in range(M)] for i in range(N)] for k in range(len(target))] # -1: 아직 계산 안됨
    for i in range(N):
        for j in range(M):
            if board[i][j] == target[0]:
                dfs(0, dp, [i, j], board, K, target, N, M)
    for i in range(N):
        for j in range(M):
            if dp[0][i][j] > 0:
                answer += dp[0][i][j]
    for i in range(N):
        print(dp[0][i])
    print(answer)


def dfs(idx, dp, pos, board, K, target, N, M):
    y, x = pos[0], pos[1]
    if idx == len(target) - 1: # 끝까지 다 도착함
        dp[idx][y][x] = 1
    else:
        nxtChar = target[idx + 1]
        tmpSum = 0
        for i in range(y - K, y + K + 1):
            if 0 <= i < N and i != y:
                if board[i][x] == nxtChar:
                    if dp[idx + 1][i][x] > 0:
                        tmpSum += dp[idx + 1][i][x]
                    elif dp[idx + 1][i][x] < 0:
                        tmpSum += dfs(idx + 1, dp, [i, x], board, K, target, N, M)
        for j in range(x - K, x + K + 1):
            if 0 <= j < M and j != x:
                if board[y][j] == nxtChar:
                    if dp[idx + 1][y][j] > 0: # 이미 결과를 구했고, 가능한 경우일때
                        tmpSum += dp[idx + 1][y][j]
                    elif dp[idx + 1][y][j] < 0:
                        tmpSum += dfs(idx + 1, dp, [y, j], board, K, target, N, M)
        dp[idx][y][x] = 0
        dp[idx][y][x] += tmpSum
    return dp[idx][y][x]


if __name__ == '__main__':
    main()
