import sys
from itertools import combinations


def main():
    global blocks, dy, dx, ansFlag
    dy, dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    t = 1
    while 1:
        N = int(sys.stdin.readline())
        vhChk = [[0 for j in range(9)] for i in range(9)]
        ansFlag = 0
        if N == 0:
            break
        board = [[0 for j in range(9)] for i in range(9)]
        blocks = list(combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
        chk = [0] * 36 # 아직 사용안한 block을 0으로 표시
        for i in range(N):
            U, LU, V, LV = map(str, sys.stdin.readline().split())
            y1, x1 = ord(LU[0]) - 65, int(LU[1]) - 1
            y2, x2 = ord(LV[0]) - 65, int(LV[1]) - 1
            U, V = int(U), int(V)
            tmp = sorted([U, V])
            board[y1][x1], board[y2][x2] = U, V
            chk[blocks.index(tuple(tmp))] = 1
        iniVal = list(map(str, sys.stdin.readline().split()))
        for i in range(9):
            y, x = ord(iniVal[i][0]) - 65, int(iniVal[i][1]) - 1
            board[y][x] = i + 1
        eFlag = 0
        print('Puzzle %s' %t)
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    backtracking(i, j, chk, board, vhChk)
                    eFlag = 1
                    break
            if eFlag:
                break
        t += 1


def backtracking(y, x, chk, board, vhChk):
    global blocks, ansFlag
    if 8 < x: # 밖으로 나갔을 때 다음 줄로 넘겨줌
        backtracking(y + 1, 0, chk, board, vhChk)
        return
    if 8 < y: # 끝까지 다 돌았음
        if ansFlag == 0:
            for i in range(9):
                for j in range(9):
                    print(board[i][j], end='')
                print()
        ansFlag = 1
        return
    if board[y][x] == 0: # 빈칸일 시에
        if y + 1 < 9 and board[y + 1][x] == 0: # 세로로 집어넣음
            for i in range(36):
                if chk[i] == 0:
                    board[y][x], board[y + 1][x] = blocks[i][0], blocks[i][1]
                    if chkV(x, board) and chkH(y, board) and chkH(y + 1, board):
                        if chkS(y, x, board) and chkS(y + 1, x, board):
                            chk[i] = 1
                            vhChk[y][x], vhChk[y + 1][x] = 1, 1
                            backtracking(y, x + 1, chk, board, vhChk)
                            vhChk[y][x], vhChk[y + 1][x] = 0, 0
                            chk[i] = 0
                    board[y][x], board[y + 1][x] = blocks[i][1], blocks[i][0]
                    if chkV(x, board) and chkH(y, board) and chkH(y + 1, board):
                        if chkS(y, x, board) and chkS(y + 1, x, board):
                            chk[i] = 1
                            vhChk[y][x], vhChk[y + 1][x] = 1, 1
                            backtracking(y, x + 1, chk, board, vhChk)
                            vhChk[y][x], vhChk[y + 1][x] = 0, 0
                            chk[i] = 0
                    board[y][x], board[y + 1][x] = 0, 0
        if x + 1 < 9 and board[y][x + 1] == 0: #가로로 집어넣음
            for i in range(36):
                if chk[i] == 0:
                    board[y][x], board[y][x + 1] = blocks[i][0], blocks[i][1]
                    if chkV(x, board) and chkV(x + 1, board) and chkH(y, board):
                        if chkS(y, x, board) and chkS(y, x + 1, board):
                            chk[i] = 1
                            vhChk[y][x], vhChk[y][x + 1] = 2, 2
                            backtracking(y, x + 1, chk, board, vhChk)
                            vhChk[y][x], vhChk[y][x + 1] = 0, 0
                            chk[i] = 0
                    board[y][x], board[y][x + 1] = blocks[i][1], blocks[i][0]
                    if chkV(x, board) and chkV(x + 1, board) and chkH(y, board):
                        if chkS(y, x, board) and chkS(y, x + 1, board):
                            chk[i] = 1
                            vhChk[y][x], vhChk[y][x + 1] = 2, 2
                            backtracking(y, x + 1, chk, board, vhChk)
                            vhChk[y][x], vhChk[y][x + 1] = 0, 0
                            chk[i] = 0
                    board[y][x], board[y][x + 1] = 0, 0
    else: # 이미 차있는 칸. 다음 칸으로 넘김
        backtracking(y, x + 1, chk, board, vhChk)


def chkV(x, board):
    chkNum = [0] * 9
    for i in range(9):
        if board[i][x] != 0:
            chkNum[board[i][x] - 1] += 1
            if chkNum[board[i][x] - 1] == 2:
                return 0
    return 1


def chkH(y, board):
    chkNum = [0] * 9
    for j in range(9):
        if board[y][j] != 0:
            chkNum[board[y][j] - 1] += 1
            if chkNum[board[y][j] - 1] == 2:
                return 0
    return 1


def chkS(y, x, board):
    global dy, dx
    chkNum = [0] * 9
    center = [3 * (y // 3) + 1, 3 * (x // 3) + 1]
    for i in range(9):
        ny, nx = center[0] + dy[i], center[1] + dx[i]
        if board[ny][nx] != 0:
            chkNum[board[ny][nx] - 1] += 1
            if chkNum[board[ny][nx] - 1] == 2:
                return 0
    return 1


if __name__ == '__main__':
    main()
