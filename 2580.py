import sys


def main():
    global board, hCnt, hole, dy, dx, flag
    board = []
    dy, dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1,], [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    for i in range(9):
        board.append(list(map(int, sys.stdin.readline().split())))
    hole = []
    hCnt = 0
    flag = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                hole.append([i, j])
                hCnt += 1
    dfs(0)


def dfs(hIdx):
    global board, hCnt, hole, dy, dx, flag
    if flag:
        return
    if hIdx == hCnt: #다 채움
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=' ')
            print()
        flag = 1
        return
    y, x = hole[hIdx][0], hole[hIdx][1]
    cy, cx = 1 + (y // 3) * 3, 1 + (x // 3) * 3
    possible= [1] * 10 #해당 hole에서 넣을수 있는 숫자
    for i in range(9):
        ny, nx = cy + dy[i], cx + dx[i]
        possible[board[ny][nx]] = 0 # 이미 있는 수이니 지운다
    for i in range(9):
        possible[board[i][x]] = 0
    for j in range(9):
        possible[board[y][j]] = 0
    for i in range(1, 10):
        if possible[i] == 1:
            board[y][x] = i
            dfs(hIdx + 1)
            board[y][x] = 0


if __name__ == '__main__':
    main()
