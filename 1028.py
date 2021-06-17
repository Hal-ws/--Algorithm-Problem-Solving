import sys


def main():
    global R, C, board
    R, C = map(int, sys.stdin.readline().split())
    board = []
    maxSize = 0
    for i in range(R):
        board.append(list(sys.stdin.readline()[:C]))
        for j in range(C):
            if board[i][j] == '1':
                maxSize = 1
    if maxSize == 0:
        print(0)
        return
    rd = [[0 for j in range(C)] for i in range(R)]
    ru = [[0 for j in range(C)] for i in range(R)]
    ld = [[0 for j in range(C)] for i in range(R)]
    lu = [[0 for j in range(C)] for i in range(R)]
    for j in range(C):
        getLength(0, j, rd, 0)
        getLength(0, j, ld, 3)
        getLength(R - 1, j, ru, 1)
        getLength(R - 1, j, lu, 2)
    for i in range(R):
        getLength(i, 0, ru, 1)
        getLength(i, 0, rd, 0)
        getLength(i, C - 1, lu, 2)
        getLength(i, C - 1, ld, 3)
    for i in range(R):
        for j in range(C):
            tmpMax = min(lu[i][j], ru[i][j])
            if tmpMax <= maxSize:
                continue
            for size in range(tmpMax, maxSize, -1):
                ny, nx = i + (size - 1) * 2, j
                if ny < R and rd[ny][nx] >= size and ld[ny][nx] >= size:
                    maxSize = size
                    break
    print(maxSize)


def getLength(y, x, lBoard, num):
    global R, C, board
    if board[y][x] == '0':
        l = 0
    else:
        l = 1
    if num == 0: # rd
        dy, dx = 1, 1
    if num == 1: # ru
        dy, dx = -1, 1
    if num == 2: # lu
        dy, dx = -1, -1
    if num == 3: # ld
        dy, dx = 1, -1
    lBoard[y][x] = l
    d = 1
    while 1:
        cy, cx = y + dy * d, x + dx * d
        if 0 <= cy < R and 0 <= cx < C:
            if board[cy][cx] == '1':
                l += 1
            else:
                l = 0
            lBoard[cy][cx] = l
            d += 1
        else:
            break


if __name__ == '__main__':
    main()
