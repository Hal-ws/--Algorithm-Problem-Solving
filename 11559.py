import sys
from collections import deque


def main():
    board = []
    answer = 0
    for i in range(12):
        board.append(list(sys.stdin.readline()[:6]))
    while 1:
        val = puyo(board)
        if val:
            answer += 1
        else:
            break
    print(answer)


def puyo(board):
    puyoChk = 0 # puyo가 있었는지 판단
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                tmp = bfs(i, j, board)
                if tmp:
                    puyoChk = 1
    if puyoChk:
        falling(board)
    return puyoChk


def bfs(sy, sx, board):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = deque()
    color = board[sy][sx]
    q.append([sy, sx])
    visit = [[0 for j in range(6)] for i in range(12)]
    visit[sy][sx] = 1
    puyoList = [[sy, sx]]
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 12 and 0 <= nx < 6 and visit[ny][nx] == 0 and board[ny][nx] == color:
                puyoList.append([ny, nx])
                visit[ny][nx] = 1
                q.append([ny, nx])
    if len(puyoList) >= 4:
        for pos in puyoList:
            y, x = pos[0], pos[1]
            board[y][x] = '.'
        return 1
    return 0


def falling(board):
    for x in range(6):
        for y in range(11, -1, -1):
            if board[y][x] != '.': # 빈칸이 아닌 걸 봤을때 밑에 떨어질 공간이 있는지 확인한후 떨어짐
                tmpY = y
                for i in range(tmpY + 1, 12):
                    if board[i][x] == '.': # 떨어질 공간 있음
                        board[i][x], board[tmpY][x] = board[tmpY][x], board[i][x]
                        tmpY += 1
                    else: #떨어질 공간 없으니 넘어감
                        break


if __name__ == "__main__":
    main()
