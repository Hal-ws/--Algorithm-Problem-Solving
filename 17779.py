import sys
from collections import deque


def main():
    N = int(sys.stdin.readline())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    minDiff = [99999999999999]
    for i in range(N - 2):
        for j in range(1, N - 1):
            dfs(board, [i, j], None, None, minDiff, N)
    print(minDiff[0])


def dfs(board, up, left, down, minDiff, N):
    if left == None:
        leftY, leftX = up[0] + 1, up[1] - 1
        while 1:
            if leftY < N - 1 and leftX >= 0:
                dfs(board, up, [leftY, leftX], None, minDiff, N)
                leftY += 1
                leftX -= 1
            else:
                break
    elif down == None:
        downY, downX = left[0] + 1, left[1] + 1
        while 1:
            if downX < N - 1 and downY < N:
                dfs(board, up, left, [downY, downX], minDiff, N)
                downY += 1
                downX += 1
            else:
                break
    else:
        rightX = (up[1] + down[0] + down[1] - up[0]) // 2
        rightY = rightX + up[0] - up[1]
        if 0 <= rightY < N and 0 <= rightX < N:
            tmp = getdiff(board, up, left, down, [rightY, rightX], N)
            if tmp <= minDiff[0]:
                minDiff[0] = tmp


def getdiff(board, up, left, down, right, N):
    area = [0, 0, 0, 0, 0]
    seperate = [[0 for i in range(N)] for j in range(N)]
    x = up[1]
    for i in range(up[0], left[0] + 1):
        y = i
        seperate[y][x] = 5
        x -= 1
    x = up[1]
    for i in range(up[0], right[0] + 1):
        y = i
        seperate[y][x] = 5
        x += 1
    x = left[1]
    for i in range(left[0], down[0] + 1):
        y = i
        seperate[y][x] = 5
        x += 1
    x = right[1]
    for i in range(right[0], down[0] + 1):
        y = i
        seperate[y][x] = 5
        x -= 1
    for i in range(up[0]):
        seperate[i][up[1]] = 1
    for j in range(right[1] + 1, N):
        seperate[right[0]][j] = 2
    for j in range(left[1]):
        seperate[left[0]][j] = 3
    for i in range(down[0] + 1, N):
        seperate[i][down[1]] = 4
    bfs(seperate, [0, 0], 1, N)
    bfs(seperate, [0, N - 1], 2, N)
    bfs(seperate, [N - 1, 0], 3, N)
    bfs(seperate, [N - 1, N - 1], 4, N)
    for i in range(N):
        for j in range(N):
            if seperate[i][j] != 5 and seperate[i][j] != 0:
                a = seperate[i][j]
                area[a - 1] += board[i][j]
            else:
                area[4] += board[i][j]
    return max(area) - min(area)


def bfs(seperate, pos, area, N):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = deque()
    chk = [[0 for i in range(N)] for j in range(N)]
    y, x = pos[0], pos[1]
    seperate[y][x] = area
    chk[y][x] = 1
    q.append([y, x])
    while len(q) > 0:
        y, x = q[0][0], q[0][1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if seperate[ny][nx] == 0 and chk[ny][nx] == 0:
                    seperate[ny][nx] = area
                    chk[ny][nx] = 1
                    q.append([ny, nx])
        q.popleft()


if __name__ == "__main__":
    main()
