import sys


def main():
    t = 1
    global dy, dx
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while 1:
        R, C = map(int, sys.stdin.readline().split())
        if R == 0 and C == 0:
            break
        board = []
        holeBoard = [[0 for j in range(C)] for i in range(R)] # hole만 표시함
        cha = [None, None]
        cFlag = 1
        for i in range(R):
            board.append(list(sys.stdin.readline()[:C]))
            for j in range(C):
                if board[i][j] == 'W' or board[i][j] == '+' or board[i][j] == 'B':
                    holeBoard[i][j] = 1
                    if board[i][j] == 'W':
                        board[i][j] = 'w'
                    if board[i][j] == 'B':
                        board[i][j] = 'b'
                    if board[i][j] == '+':
                        board[i][j] = '.'
                if board[i][j] == 'w':
                    cha[0], cha[1] = i, j
        tmp = sys.stdin.readline()
        command = []
        for i in range(len(tmp) - 1):
            if tmp[i] == 'U':
                command.append(0)
            if tmp[i] == 'D':
                command.append(1)
            if tmp[i] == 'L':
                command.append(2)
            if tmp[i] == 'R':
                command.append(3)
        for i in range(len(command)):
            result = move(board, cha, command[i])
            board = result[0]
            cha = result[1]
            eFlag = 1
            for j in range(R):
                for k in range(C):
                    if board[j][k] == 'b' and holeBoard[j][k] != 1:
                        eFlag = 0
            if eFlag:
                break
        for i in range(R):
            for j in range(C):
                if holeBoard[i][j]:
                    if board[i][j] == 'b':
                        board[i][j] = 'B'
                    else:
                        if board[i][j] == '.':
                            board[i][j] = '+'
                        if board[i][j] == 'w':
                            board[i][j] = 'W'
                        cFlag = 0
        if cFlag:
            print("Game %s: complete" %t)
        else:
            print("Game %s: incomplete" %t)
        for i in range(R):
            for j in range(C):
                print(board[i][j], end='')
            print()
        t += 1


def move(board, cha, d):
    global dy, dx
    y, x = cha[0], cha[1]
    ny, nx = y + dy[d], x + dx[d]
    if board[ny][nx] == '#': #못움직임
        cha = [y, x] # 그대로
    if board[ny][nx] == '.' or board[ny][nx] == '+': # 움직일 수 있을 때. hole은 신경안씀
        board[ny][nx] = 'w'
        board[y][x] = '.'
        cha = [ny, nx]
    if board[ny][nx] == 'b': # box일 때
        my, mx = y + (dy[d] * 2), x + (dx[d] * 2)
        if board[my][mx] == '.' or board[my][mx] == '+':
            board[my][mx] = 'b'
            board[ny][nx] = 'w'
            board[y][x] = '.'
            cha = [ny, nx]
    return [board, cha]


if __name__ == '__main__':
    main()
