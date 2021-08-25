import sys


def main():
    global N, M, K, board, dp, target, dy, dx
    N, M, K = map(int, sys.stdin.readline().split())
    board = []
    answer = 0
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for i in range(N):
        board.append(sys.stdin.readline()[:M])
    target = sys.stdin.readline()
    target = target[:len(target) - 1]
    dp = [[[-1 for j in range(M)] for i in range(N)] for k in range(len(target))] # -1: 아직 계산 안됨
    for i in range(N):
        for j in range(M):
            if board[i][j] == target[0]:
                answer += dfs(0, i, j)
    print(answer)


def dfs(idx, y, x):
    global N, M, K, board, dp, target, dy, dx
    if board[y][x] != target[idx]:
        return 0
    if idx == len(target) - 1: # 끝까지 도달
        dp[idx][y][x] = 1
        return 1
    if dp[idx][y][x] != -1:
        return dp[idx][y][x]
    dp[idx][y][x] = 0
    for d in range(4):  # 4방향
        for i in range(1, K + 1):
            ny, nx = y + (dy[d] * i), x + (dx[d] * i)
            if 0 <= ny < N and 0 <= nx < M:
                dp[idx][y][x] += dfs(idx + 1, ny, nx)
    return dp[idx][y][x]


if __name__ == '__main__':
    main()
