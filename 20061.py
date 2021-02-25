import sys


def main():
    global board, score
    N = int(sys.stdin.readline())
    board = [[0 for j in range(10)] for i in range(10)]
    score = 0
    cnt = 0
    for i in range(4, 10):
        for j in range(4, 10):
            board[i][j] = 8
    for i in range(N):
        t, y, x = map(int, sys.stdin.readline().split())
        moveright(t, y, x)
        movedown(t, y, x)
        greenpop()
        bluepop()
        lightgreen()
        lightblue()
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                cnt += 1
    print(score)
    print(cnt)


def moveright(t, y, x):
    global board
    if t == 1: # 1x1이 오른쪽으로 움직임
        for j in range(x + 1, 10):
            if board[y][j] == 1: # 다른 block이 이미 차 있음
                ny, nx = y, j - 1
                break
            if board[y][j] == 0 and j == 9: #끝까지 도착
                ny, nx = y, j
        board[ny][nx] = 1
    if t == 2: # 1x2가 오른쪽으로 움직임
        for j in range(x + 2, 10):
            if board[y][j] == 1:
                ny, nx = y, j - 2
                break
            if board[y][j] == 0 and j == 9:
                ny, nx = y, j - 1
        board[ny][nx], board[ny][nx + 1] = 1, 1
    if t == 3: # 2x1
        for j in range(x + 1, 10):
            if board[y][j] == 1 or board[y + 1][j] == 1:
                ny, nx = y, j - 1
                break
            if board[y][j] == 0 and board[y + 1][j] == 0 and j == 9:
                ny, nx = y, j
        board[ny][nx], board[ny + 1][nx] = 1, 1


def movedown(t, y, x):
    global board
    if t == 1: # 1x1
        for i in range(y + 1, 10):
            if board[i][x] == 1:
                ny, nx = i - 1, x
                break
            if board[i][x] == 0 and i == 9:
                ny, nx = i, x
        board[ny][nx] = 1
    if t == 2: #1x2
        for i in range(y + 1, 10):
            if board[i][x] == 1 or board[i][x + 1] == 1:
                ny, nx = i - 1, x
                break
            if board[i][x] == 0 and board[i][x + 1] == 0 and i == 9:
                ny, nx = 9, x
        board[ny][nx], board[ny][nx + 1] = 1, 1
    if t == 3: #2x1
        for i in range(y + 2, 10):
            if board[i][x] == 1:
                ny, nx = i - 2, x
                break
            if board[i][x] == 0 and i == 9:
                ny, nx = i - 1, x
        board[ny][nx], board[ny + 1][nx] = 1, 1


def greenpop():
    global board, score 
    for i in range(6, 10):
        flag = 1
        for j in range(4):
            if board[i][j] == 0:
                flag = 0
                break
        if flag: # pop
            score += 1
            board[i][0], board[i][1], board[i][2], board[i][3] = 0, 0, 0, 0
            for ii in range(i, 4, -1):
                for j in range(4):
                    board[ii][j] = board[ii - 1][j] # 내려옴


def bluepop():
    global board, score
    for j in range(6, 10):
        flag = 1
        for i in range(4):
            if board[i][j] == 0:
                flag = 0
                break
        if flag:
            score += 1
            board[0][j], board[1][j], board[2][j], board[3][j] = 0, 0, 0, 0
            for jj in range(j, 4, -1):
                for i in range(4):
                    board[i][jj] = board[i][jj - 1] # 오른쪽으로 움직임
    return 0

def lightgreen():
    global board
    mvCnt = 0 #몇칸 지울지 결정
    for i in range(4, 6):
        for j in range(4):
            if board[i][j] == 1:
                mvCnt += 1
                break
    if mvCnt != 0:
        for i in range(9, 3, -1):
            for j in range(4):
                board[i][j] = board[i - mvCnt][j]


def lightblue():
    global board
    mvCnt = 0
    for j in range(4, 6):
        for i in range(4):
            if board[i][j] == 1:
                mvCnt += 1
                break
    if mvCnt != 0:
        for j in range(9, 3, -1):
            for i in range(4):
                board[i][j] = board[i][j - mvCnt]


if __name__ == '__main__':
    main()
