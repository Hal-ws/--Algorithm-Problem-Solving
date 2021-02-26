import sys
from itertools import combinations


def main():
    global board, garo, sero, box, flag, blocks
    t = 1
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
                    if chkPossible(blocks[k], 0): # 그대로 가능
                        possIdx[k] = 0
                        backtraking(y, x + 2, emptyCnt - 2, possIdx)
                        possIdx[k] = 1
                    if chkPossible(blocks[k], 1): # 뒤집은게 가능
                        possIdx[k] = 0
                        backtraking(y, x + 2, emptyCnt - 2, possIdx)
                        possIdx[k] = 1
                

    for i in range(y + 1, 9):
        for j in range(9):
            return


def chkPossible(domino, rFlag):
    global board
    return


if __name__ == '__main__':
    main()
