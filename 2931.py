import sys


def main():
    global R, C, board, dy, dx
    R, C = map(int, sys.stdin.readline().split())
    board = []
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(R):
        board.append(list(sys.stdin.readline()[:C]))
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'M':
                mos = [i, j]
            if board[i][j] == 'Z':
                zag = [i, j]
    ePos = follow(mos)
    y, x = ePos[0], ePos[1]
    connect = [0, 0, 0, 0]
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < R and 0 <= nx < C:
            if i == 0:
                if board[ny][nx] == '+' or board[ny][nx] == '|' or board[ny][nx] == '1' or board[ny][nx] == '4':
                    connect[i] = 1
            if i == 1:
                if board[ny][nx] == '+' or board[ny][nx] == '|' or board[ny][nx] == '2' or board[ny][nx] == '3':
                    connect[i] = 1
            if i == 2:
                if board[ny][nx] == '+' or board[ny][nx] == '-' or board[ny][nx] == '1' or board[ny][nx] == '2':
                    connect[i] = 1
            if i == 3:
                if board[ny][nx] == '+' or board[ny][nx] == '-' or board[ny][nx] == '3' or board[ny][nx] == '4':
                    connect[i] = 1
    if connect == [1, 1, 0, 0]:
        ansPipe = '|'
    if connect == [0, 0, 1, 1]:
        ansPipe = '-'
    if connect == [1, 1, 1, 1]:
        ansPipe = '+'
    if connect == [0, 1, 0, 1]:
        ansPipe = '1'
    if connect == [1, 0, 0, 1]:
        ansPipe = '2'
    if connect == [1, 0, 1, 0]:
        ansPipe = '3'
    if connect == [0, 1, 1, 0]:
        ansPipe = '4'
    print('%s %s %s' %(y + 1, x + 1, ansPipe))



def follow(city):
    global R, C, board, dy, dx
    cur = [None, None, None] #현 좌표 / 들어온 방향
    y, x = city[0], city[1]
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < R and 0 <= nx < C:
            if i == 0: # 상
                if board[ny][nx] == '1' or board[ny][nx] == '4' or board[ny][nx] == '|' or board[ny][nx] == '+':
                    cur = [ny, nx, i]
            if i == 1: # 하
                if board[ny][nx] == '2' or board[ny][nx] == '3' or board[ny][nx] == '|' or board[ny][nx] == '+':
                    cur = [ny, nx, i]
            if i == 2: # 좌
                if board[ny][nx] == '1' or board[ny][nx] == '2' or board[ny][nx] == '-' or board[ny][nx] == '+':
                    cur = [ny, nx, i]
            if i == 3: # 우
                if board[ny][nx] == '3' or board[ny][nx] == '4' or board[ny][nx] == '-' or board[ny][nx] == '+':
                    cur = [ny, nx, i]
    while 1:
        y, x, d = cur[0], cur[1], cur[2]
        pipe = board[y][x]
        if pipe == '|':
            if d == 0: # 올라가는거일때
                if board[y - 1][x] == '.':
                    return [y - 1, x]
                else:
                    cur = [y - 1, x, d]
            if d == 1:
                if board[y + 1][x] == '.':
                    return [y + 1, x]
                else:
                    cur = [y + 1, x, d]
        if pipe == '-':
            if d == 2:
                if board[y][x - 1] == '.':
                    return [y, x - 1]
                else:
                    cur = [y, x - 1, d]
            if d == 3:
                if board[y][x + 1] == '.':
                    return [y, x + 1]
                else:
                    cur = [y, x + 1, d]
        if pipe == '+':
            if d == 0:
                if board[y - 1][x] == '.':
                    return [y - 1, x]
                else:
                    cur = [y - 1, x, d]
            if d == 1:
                if board[y + 1][x] == '.':
                    return [y + 1, x]
                else:
                    cur = [y + 1, x, d]
            if d == 2:
                if board[y][x - 1] == '.':
                    return [y, x - 1]
                else:
                    cur = [y, x - 1, d]
            if d == 3:
                if board[y][x + 1] == '.':
                    return [y, x + 1]
                else:
                    cur = [y, x + 1, d]
        if pipe == '1':
            if d == 0:
                if board[y][x + 1] == '.':
                    return [y, x + 1]
                else:
                    cur = [y, x + 1, 3]
            if d == 2:
                if board[y + 1][x] == '.':
                    return [y + 1, x]
                else:
                    cur = [y + 1, x, 1]
        if pipe == '2':
            if d == 1:
                if board[y][x + 1] == '.':
                    return [y, x + 1]
                else:
                    cur = [y, x + 1, 3]
            if d == 2:
                if board[y - 1][x] == '.':
                    return [y - 1, x]
                else:
                    cur = [y - 1, x, 0]
        if pipe == '3':
            if d == 3:
                if board[y - 1][x] == '.':
                    return [y - 1, x]
                else:
                    cur = [y - 1, x, 0]
            if d == 1:
                if board[y][x - 1] == '.':
                    return [y, x - 1]
                else:
                    cur = [y, x - 1, 2]
        if pipe == '4':
            if d == 3:
                if board[y + 1][x] == '.':
                    return [y + 1, x]
                else:
                    cur = [y + 1, x, 1]
            if d == 0:
                if board[y][x - 1] == '.':
                    return [y, x - 1]
                else:
                    cur = [y, x - 1, 2]


if __name__ == '__main__':
    main()
