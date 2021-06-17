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
        getrd(0, j, rd)
        getld(0, j, ld)
        getru(R - 1, j, ru)
        getlu(R - 1, j, lu)
    for i in range(R):
        getru(i, 0, ru)
        getrd(i, 0, rd)
        getlu(i, C - 1, lu)
        getld(i, C - 1, ld)
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


def getrd(y, x, rd):
    global R, C, board
    d = 1
    if board[y][x] == '0':
        l = 0
    else:
        l = 1
    rd[y][x] = l
    while 1:
        cy, cx = y + d, x + d
        if 0 <= cy < R and 0 <= cx < C:
            if board[cy][cx] == '1':
                l += 1
            else:
                l = 0
            rd[cy][cx] = l
            d += 1
        else:
            break


def getru(y, x, ru):
    global R, C, board
    d = 1
    if board[y][x] == '0':
        l = 0
    else:
        l = 1
    ru[y][x] = l
    while 1:
        cy, cx = y - d, x + d
        if 0 <= cy < R and 0 <= cx < C:
            if board[cy][cx] == '1':
                l += 1
            else:
                l = 0
            ru[cy][cx] = l
            d += 1
        else:
            break


def getlu(y, x, lu):
    global R, C, board
    d = 1
    if board[y][x] == '0':
        l = 0
    else:
        l = 1
    lu[y][x] = l
    while 1:
        cy, cx = y - d, x - d
        if 0 <= cy < R and 0 <= cx < C:
            if board[cy][cx] == '1':
                l += 1
            else:
                l = 0
            lu[cy][cx] = l
            d += 1
        else:
            break


def getld(y, x, ld):
    global R, C, board
    d = 1
    if board[y][x] == '0':
        l = 0
    else:
        l = 1
    ld[y][x] = l
    while 1:
        cy, cx = y + d, x - d
        if 0 <= cy < R and 0 <= cx < C:
            if board[cy][cx] == '1':
                l += 1
            else:
                l = 0
            ld[cy][cx] = l
            d += 1
        else:
            break


if __name__ == '__main__':
    main()
