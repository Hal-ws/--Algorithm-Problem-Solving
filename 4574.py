import sys
from itertools import combinations


def main():
    global board, garo, sero, box, flag, blocks, dy, dx
    t = 1
    dy, dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    while 1:
        N = int(sys.stdin.readline())
        if N == 0:
            break
        print('Puzzle %s' %t)
        emptyCnt = 81 - 2 * N - 9
        flag = 0
        board = [[0 for j in range(9)] for i in range(9)]
        tmp = list(combinations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 2))
        possIdx = [1] * 45
        blocks = [] # 사용 가능한 블록
        for b in tmp:
            b = list(b)
            b.sort()
            blocks.append(b[0] + b[1])
        for i in range(N):
            U, LU, V, LV = map(str, sys.stdin.readline().split())
            y1, x1 = ord(LU[0]) - 65, int(LU[1]) - 1
            y2, x2 = ord(LV[0]) - 65, int(LV[1]) - 1
            tmp = sorted([U, V])
            possIdx[blocks.index(tmp[0] + tmp[1])] = 0
            board[y1][x1] = U
            board[y2][x2] = V
        numPos = list(map(str, sys.stdin.readline().split()))
        for i in range(9):
            y, x = ord(numPos[i][0]) - 65, int(numPos[i][1]) - 1
            board[y][x] = str(i + 1)
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0: #빈칸 채워줌
                    backtraking(i, j, emptyCnt, blocks, possIdx)
        for i in range(9):
            for j in range(9):
                print(board[i][j], end='')
            print()
        t += 1


def backtraking(y, x, emptyCnt, possIdx):
    global board, garo, sero, box, flag, blocks
    if emptyCnt == 0:
        flag = 1
        return
    if flag:
        return
    for j in range(x, 9):
        if board[y][j] == 0: #
            if j < 8 and board[y][j + 1] == 0: # 가로로 넣어봄
                for k in range(45):
                    if possIdx[k]: # 쓸수 있는 block일때
                        if chkPossible(y, j, blocks[k], 0, 0): # 그대로 가능
                            possIdx[k] = 0
                            board[y][j], board[y][j + 1] = blocks[k][0], blocks[k][1]
                            backtraking(y, j + 2, emptyCnt - 2, possIdx)
                            board[y][j], board[y][j + 1] = 0, 0
                            possIdx[k] = 1
                        if chkPossible(y, j, blocks[k], 0, 1): # 뒤집은게 가능
                            possIdx[k] = 0
                            board[y][j], board[y][j + 1] = blocks[k][1], blocks[k][0]
                            backtraking(y, j + 2, emptyCnt - 2, possIdx)
                            board[y][j], board[y][j + 1] = 0, 0
                            possIdx[k] = 1
            if y < 8 and board[y + 1][j] == 0: #세로로 넣어봄
                for k in range(45):
                    if possIdx[k]:
                        if chkPossible(y, j, blocks[k], 1, 0):
                            possIdx[k] = 0
                            board[y][j], board[y + 1][j] = blocks[k][0], blocks[k][1]
                            backtraking(y + 2, j, emptyCnt - 2, possIdx)
                            board[y][j], board[y + 1][j] = 0, 0
                            possIdx[k] = 1
                        if chkPossible(y, j, blocks[k], 1, 1):
                            possIdx[k] = 0
                            board[y][j], board[y + 1][j] = blocks[k][1], blocks[k][0]
                            backtraking(y + 2, j, emptyCnt - 2, possIdx)
                            board[y][j], board[y + 1][j] = 0, 0
                            possIdx[k] = 1
    for i in range(y + 1, 9):
        for j in range(9):
            if j < 8 and board[i][j + 1] == 0: # 가로로 넣어봄
                for k in range(45):
                    if possIdx[k]: # 쓸수 있는 block일때
                        if chkPossible(i, j, blocks[k], 0, 0): # 그대로 가능
                            possIdx[k] = 0
                            board[i][j], board[i][j + 1] = blocks[k][0], blocks[k][1]
                            backtraking(i, j + 2, emptyCnt - 2, possIdx)
                            board[i][j], board[i][j + 1] = 0, 0
                            possIdx[k] = 1
                        if chkPossible(i, j, blocks[k], 0, 1): # 뒤집은게 가능
                            possIdx[k] = 0
                            board[i][j], board[i][j + 1] = blocks[k][1], blocks[k][0]
                            backtraking(i, j + 2, emptyCnt - 2, possIdx)
                            board[i][j], board[i][j + 1] = 0, 0
                            possIdx[k] = 1
            if y < 8 and board[y + 1][j] == 0: #세로로 넣어봄
                for k in range(45):
                    if possIdx[k]:
                        if chkPossible(i, j, blocks[k], 1, 0):
                            possIdx[k] = 0
                            board[i][j], board[i + 1][j] = blocks[k][0], blocks[k][1]
                            backtraking(i + 2, j, emptyCnt - 2, possIdx)
                            blocks[i][j], blocks[i + 1][j] = 0, 0
                            possIdx[k] = 1
                        if chkPossible(i, j, blocks[k], 1, 1):
                            possIdx[k] = 0
                            board[i][j], board[i + 1][j] = blocks[k][1], blocks[k][0]
                            backtraking(i + 2, j, emptyCnt - 2, possIdx)
                            board[i][j], board[i + 1][j] = 0, 0
                            possIdx[k] = 1


def chkPossible(y, x, domino, vFlag, rFlag): #도미노, 가로세로 구분, 뒤집는것
    global board, dy, dx
    if rFlag:
        domino = domino[::-1]
    c1 = [1 + (y // 3) * 3, 1 + (x // 3) * 3]
    if vFlag:
        for j in range(9):
            if board[y][j] == domino[0]:
                return 0
            if board[y + 1][j] == domino[1]:
                return 0
        for i in range(9):
            if board[i][x] == domino[0] or board[i][x] == domino[1]:
                return 0
        c2 = [1 + ((y + 1) // 3) * 3, 1 + (x // 3) * 3]
    else:
        for j in range(9):
            if board[y][j] == domino[0] or board[y][j] == domino[1]:
                return 0
        for i in range(9):
            if board[i][x] == domino[0]:
                return 0
            if board[i][x + 1] == domino[1]:
                return 0
        c2 = [1 + (y // 3) * 3, 1 + ((x + 1) // 3) * 3]
    return 1


    return


if __name__ == '__main__':
    main()
