import sys


def main():
    global dy, dx, ans
    dy, dx = [-1, -1, 0, 0, 1, 1], [-1, 1, -2, 2, -1, 1]
    board = []
    chk = [0] * 12 # 사용한 것
    ans = 'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL'
    for i in range(5):
        board.append(list(sys.stdin.readline()[:9]))
    for i in range(5):
        for j in range(9):
            tmp = ord(board[i][j]) - 65
            if 0 <= tmp <= 11:
                chk[tmp] = 1
            board[i][j] = tmp + 1
    if board[0][4] != 56:
        dfs(board, 4, chk, 0, 4)
    else:
        for i in range(12):
            if chk[i] == 0:
                chk[i] = 1
                board[0][4] = i + 1
                dfs(board, 4, chk, 0, 4)
                chk[i] = 0
                board[0][4] = '.'
    for i in range(5):
        print(ans[i * 9:i * 9 + 9])


def dfs(board, d, chk, y, x):
    global dy, dx, ans
    if y == 1 and x == 7: # end position arrive
        sum1 = board[1][7] + board[1][5] + board[1][3] + board[1][1]
        sum2 = board[1][7] + board[2][6] + board[3][5] + board[4][4]
        if sum1 == 26 and sum2 == 26:
            tmpans = ''
            for i in range(5):
                for j in range(9):
                    tmpans += chr(board[i][j] + 64)
            if tmpans < ans:
                ans = tmpans
        return
    if y == 3 and x == 1:
        tSum = board[3][1] + board[2][2] + board[1][3] + board[0][4]
        if tSum != 26:
            return
        d = 3
    if y == 3 and x == 7:
        tSum = board[3][1] + board[3][3] + board[3][5] + board[3][7]
        if tSum != 26:
            return
        d = 0
    if y == 1 and x == 5:
        tSum = board[0][4] + board[1][5] + board[2][6] + board[3][7]
        if tSum != 26:
            return
        d = 2
    if y == 1 and x == 1:
        if board[1][7] != 56:
            tSum = board[1][1] + board[1][3] + board[1][5] + board[1][7]
            if tSum != 26:
                return
        d = 5
    if y == 4 and x == 4:
        tSum = board[1][1] + board[2][2] + board[3][3] + board[4][4]
        if tSum != 26:
            return
        d = 1
    ny, nx = y + dy[d], x + dx[d]
    if board[ny][nx] != 56: #이미 차있음
        dfs(board, d, chk, ny, nx)
    else:
        for i in range(12):
            if chk[i] == 0: #비었을때
                chk[i] = 1
                board[ny][nx] = i + 1
                dfs(board, d, chk, ny, nx)
                chk[i] = 0
                board[ny][nx] = 56
    return


if __name__ == '__main__':
    main()
