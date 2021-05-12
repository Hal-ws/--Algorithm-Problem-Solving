import sys


def main():
    while 1:
        tic = sys.stdin.readline()[:9]
        if tic[0] == 'e':
            break
        print(chkvalid(tic))


def chkvalid(tic):
    board = [[0 for j in range(3)] for i in range(3)]
    for i in range(9):
        board[i // 3][i % 3] = tic[i]
    xCnt, oCnt = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                xCnt += 1
            if board[i][j] == 'O':
                oCnt += 1
    if xCnt > oCnt + 1:
        return 'invalid'
    if xCnt < oCnt:
        return 'invalid'
    xEnd, oEnd = endChk(board, 'X'), endChk(board, 'O')
    if xEnd == 1 and oEnd == 0:
        if xCnt == oCnt + 1:
            return 'valid'
        else:
            return 'invalid'
    elif xEnd == 0 and oEnd == 1:
        if xCnt == oCnt:
            return 'valid'
        else:
            return 'invalid'
    elif xEnd == 0 and oEnd == 0:
        if xCnt + oCnt == 9:
            return 'valid'
        else:
            return 'invalid'
    else:
        return 'invalid'


def endChk(board, std):
    cnt = 0
    # 가로줄 점검
    for i in range(3):
        flag = 1
        for j in range(3):
            if board[i][j] != std:
                flag = 0
                break
        if flag:
            cnt += 1
            for j in range(3):
                board[i][j] = '.' # cnt가 끝난 값이니 비워준다(중복 제거)
    for j in range(3):
        flag = 1
        for i in range(3):
            if board[i][j] != std:
                flag = 0
                break
        if flag:
            cnt += 1
            for i in range(3):
                board[i][j] = '.'
    flag = 1
    for i in range(3):
        if board[i][i] != std:
            flag = 0
            break
    if flag:
        cnt += 1
        for i in range(3):
            board[i][i] = '.'
    flag = 1
    for i in range(3):
        if board[2 - i][i] != std:
            flag = 0
            break
    if flag:
        cnt += 1
        for i in range(3):
            board[2 - i][i] = '.'
    return cnt


if __name__ == '__main__':
    main()
