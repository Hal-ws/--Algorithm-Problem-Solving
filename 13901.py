import sys


def main():
    R, C = map(int, sys.stdin.readline().split())
    board = [[0 for j in range(C)] for i in range(R)]
    visit = [[0 for j in range(C)] for i in range(R)]
    dy, dx = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
    k = int(sys.stdin.readline())
    for i in range(k):
        y, x = map(int, sys.stdin.readline().split())
        board[y][x] = 1 #장애물은 1로 표시
    sy, sx = map(int, sys.stdin.readline().split())
    dList = list(map(int, sys.stdin.readline().split()))
    visit[sy][sx] = 1
    y, x = sy, sx
    dIdx = 0
    while 1:
        dIdx = dIdx % 4
        ny, nx = y + dy[dList[dIdx]], x + dx[dList[dIdx]]
        flag = 0
        if 0 <= ny < R and 0 <= nx < C and visit[ny][nx] == 0 and board[ny][nx] == 0:
            y, x = ny, nx
            visit[y][x] = 1
            flag = 1
            continue
        dIdx += 1
        dIdx = dIdx % 4
        ny, nx = y + dy[dList[dIdx]], x + dx[dList[dIdx]]
        if 0 <= ny < R and 0 <= nx < C and visit[ny][nx] == 0 and board[ny][nx] == 0:
            y, x = ny, nx
            visit[y][x] = 1
            flag = 1
            continue
        dIdx += 1
        dIdx = dIdx % 4
        ny, nx = y + dy[dList[dIdx]], x + dx[dList[dIdx]]
        if 0 <= ny < R and 0 <= nx < C and visit[ny][nx] == 0 and board[ny][nx] == 0:
            y, x = ny, nx
            visit[y][x] = 1
            flag = 1
            continue
        dIdx += 1
        dIdx = dIdx % 4
        ny, nx = y + dy[dList[dIdx]], x + dx[dList[dIdx]]
        if 0 <= ny < R and 0 <= nx < C and visit[ny][nx] == 0 and board[ny][nx] == 0:
            y, x = ny, nx
            visit[y][x] = 1
            flag = 1
            continue
        if flag == 0:
            break
    print('%s %s' %(y, x))


if __name__ == '__main__':
    main()

