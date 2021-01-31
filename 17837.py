import sys


def main():
    global N, K, color, horses, board, dy, dx
    N, K = map(int, sys.stdin.readline().split())
    board = [[[] for j in range(N)] for i in range(N)]
    color = []
    horses = [0] * K
    flag = 0
    dy, dx = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
    for i in range(N):
        color.append(list(map(int, sys.stdin.readline().split())))
    for i in range(K):
        y, x, d = map(int, sys.stdin.readline().split())
        y, x = y - 1, x - 1
        horses[i] = [y, x, d]
        board[y][x].append(i) # i번 저장
    for t in range(1, 1001):
        if moving():
            flag = 1
            ans = t
            break
    if flag:
        print(ans)
    else:
        print(-1)


def moving():
    global N, K, color, horses, board, dy, dx
    for i in range(K):
        y, x, d = horses[i][0], horses[i][1], horses[i][2]
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < N and 0 <= nx < N: #들어갈때
            if color[ny][nx] == 0:
                towhite(i, d)
            if color[ny][nx] == 1:
                tored(i, d)
            if len(board[ny][nx]) >= 4:
                return 1
            if color[ny][nx] == 2:
                toblue(i, d)
                if d == 1 and x > 0 and color[y][x - 1] != 2:
                    if len(board[y][x - 1]) >= 4:
                        return 1
                if d == 2 and x < N - 1 and color[y][x + 1] != 2:
                    if len(board[y][x + 1]) >= 4:
                        return 1
                if d == 3 and y < N - 1 and color[y + 1][x] != 2:
                    if len(board[y + 1][x]) >= 4:
                        return 1
                if d == 4 and y > 0 and color[y - 1][x] != 2:
                    if len(board[y - 1][x]) >= 4:
                        return 1
        else:
            toblue(i, d)
            if d == 1 and x > 0 and color[y][x - 1] != 2:
                if len(board[y][x - 1]) >= 4:
                    return 1
            if d == 2 and x < N - 1 and color[y][x + 1] != 2:
                if len(board[y][x + 1]) >= 4:
                    return 1
            if d == 3 and y < N - 1 and color[y + 1][x] != 2:
                if len(board[y + 1][x]) >= 4:
                    return 1
            if d == 4 and y > 0 and color[y - 1][x] != 2:
                if len(board[y - 1][x]) >= 4:
                    return 1
    return 0


def towhite(idx, d):
    global N, K, color, horses, board, ny, nx
    y, x = horses[idx][0], horses[idx][1]
    ny, nx = y + dy[d], x + dx[d]
    tIdx = board[y][x].index(idx) #idx 의 높이 구함
    for i in range(tIdx, len(board[y][x])): # 쌓인 말 옮기기 시작
        hIdx = board[y][x][i] #움직이는 말의 idx
        horses[hIdx] = [ny, nx, horses[hIdx][2]]
        board[ny][nx].append(hIdx)
    board[y][x] = board[y][x][:tIdx]


def tored(idx, d):
    global N, K, color, horses, board, ny, nx
    y, x = horses[idx][0], horses[idx][1]
    ny, nx = y + dy[d], x + dx[d]
    tIdx = board[y][x].index(idx)
    tmpH = []
    for i in range(tIdx, len(board[y][x])):
        hIdx = board[y][x][i]
        horses[hIdx] = [ny, nx, horses[hIdx][2]]
        tmpH.append(hIdx)
    board[ny][nx] += reversed(tmpH)
    board[y][x] = board[y][x][:tIdx]


def toblue(idx, d):
    global N, K, color, horses, board, ny, nx
    y, x = horses[idx][0], horses[idx][1]
    if d == 1:
        horses[idx][2] = 2
        if x - 1 >= 0:
            if color[y][x - 1] == 0:
                towhite(idx, 2)
            if color[y][x - 1] == 1:
                tored(idx, 2)
    if d == 2:
        horses[idx][2] = 1
        if x + 1 < N:
            if color[y][x + 1] == 0:
                towhite(idx, 1)
            if color[y][x + 1] == 1:
                tored(idx, 1)
    if d == 3:
        horses[idx][2] = 4
        if y + 1 < N:
            if color[y + 1][x] == 0:
                towhite(idx, 4)
            if color[y + 1][x] == 1:
                tored(idx, 4)
    if d == 4:
        horses[idx][2] = 3
        if y - 1 >= 0:
            if color[y - 1][x] == 0:
                towhite(idx, 3)
            if color[y - 1][x] == 1:
                tored(idx, 3)


if __name__ == '__main__':
    main()
