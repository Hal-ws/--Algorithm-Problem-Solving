import sys


def main():
    global board, cloud, N, dy, dx
    N, M = map(int, sys.stdin.readline().split())
    board = [[0 for j in range(N + 1)]] # 바구니 표시
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    for i in range(N):
        tmp = [0] + list(map(int, sys.stdin.readline().split()))
        board.append(tmp)
    cloud = [[0 for j in range(N + 1)] for i in range(N + 1)] # 구름 표시. 3번 과정에서 삭제된 칸은 -1로 표시
    cloud[N][1], cloud[N][2], cloud[N - 1][1], cloud[N - 1][2] = 1, 1, 1, 1
    for i in range(M):
        command = list(map(int, sys.stdin.readline().split()))
        bibaragi(command)
    answer = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            answer += board[i][j]
    print(answer)


def bibaragi(command):
    moveCloud(command[0], command[1])
    raining()
    watercopy()
    makeCloud()


def moveCloud(d, s):
    global board, cloud, N
    nxtCloud = [[0 for j in range(N + 1)] for i in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if cloud[i][j] == 1: # 이동해야하는 구름이 있으면
                y, x = i, j
                for k in range(s): # s번 움직임
                    y, x = y + dy[d - 1], x + dx[d - 1]
                    if y == 0:
                        y = N
                    if x == 0:
                        x = N
                    if y == N + 1:
                        y = 1
                    if x == N + 1:
                        x = 1
                nxtCloud[y][x] = 2 # 이동한 구름은 2로 표시
                cloud[i][j] = 0
    cloud = nxtCloud


def raining():
    global board, cloud, N
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if cloud[i][j] == 2:
                board[i][j] += 1
                cloud[i][j] = -1 # 구름 삭제. 삭제된 칸이니까 -1로 표시한다


def watercopy():
    global board, cloud, N, dy, dx
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if cloud[i][j] == -1:
                cnt = 0
                for k in range(1, 8, 2):
                    ny, nx = i + dy[k], j + dx[k]
                    if 1 <= ny < N + 1 and 1 <= nx < N + 1 and board[ny][nx] > 0: # 범위 안이고 물이 있을 시
                        cnt += 1
                board[i][j] += cnt

def makeCloud():
    global board, cloud, N
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if cloud[i][j] == -1:
                cloud[i][j] = 0
            else:
                if board[i][j] >= 2:
                    board[i][j] -= 2
                    cloud[i][j] = 1


if __name__ == '__main__':
    main()
