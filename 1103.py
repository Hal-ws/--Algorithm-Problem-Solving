import sys


def main():
    global N, M, result, dy, dx, board
    sys.setrecursionlimit(2501)
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(sys.stdin.readline()[:M]))
        for j in range(M):
            if board[i][j] != 'H':
                board[i][j] = int(board[i][j])
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    result = [[0 for j in range(M)] for i in range(N)]
    visit = [[0 for j in range(M)] for i in range(N)]
    ans = 0
    visit[0][0] = 1
    getSol([0, 0], visit)
    for i in range(N):
        for j in range(M):
            if result[i][j] > ans:
                ans = result[i][j]
    print(ans)


def getSol(pos, visit): # 시작 좌표, 지나온 좌표들
    global N, M, result, dy, dx, board
    y, x = pos[0], pos[1]
    if visit[y][x] == 2:
        print(-1)
        sys.exit()
    maxVal = 0
    for i in range(4):
        ny, nx = y + (dy[i] * board[y][x]), x + (dx[i] * board[y][x])
        if 0 <= ny < N and 0 <= nx < M and board[ny][nx] != 'H':
            if result[ny][nx] != 0: # 이미 계산한 값 존재
                if maxVal < result[ny][nx]:
                    maxVal = result[ny][nx]
            else:
                visit[ny][nx] += 1
                tmp = getSol([ny, nx], visit)
                visit[ny][nx] -= 1
                if maxVal < tmp:
                    maxVal = tmp
    if maxVal > 0: # 다음으로 진행가능
        result[y][x] = 1 + maxVal
    else: # 더 갈곳 없음. 여기에 놓으면 1임
        result[y][x] = 1
    return result[y][x]


if __name__ == '__main__':
    main()
