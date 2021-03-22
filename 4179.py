import sys
from collections import deque


def main():
    global R, C, board, dy, dx
    R, C = map(int, sys.stdin.readline().split())
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    board = []
    fire = []
    for i in range(R):
        board.append(list(sys.stdin.readline()[:C]))
        for j in range(C):
            if board[i][j] == 'J':
                start = [i, j, 0, 0]
            if board[i][j] == 'F':
                fire.append([i, j, 1])
    print(escape(start, fire))


def escape(jihoon, fire):
    global R, C, board, dy, dx
    visit = [[0 for j in range(C)] for i in range(R)]
    q = deque()
    visit[jihoon[0]][jihoon[1]] = 1 # jihoon 은 1로 표시
    q.append(jihoon)
    for f in fire:
        y, x = f[0], f[1]
        visit[y][x] = 2
        q.append(f)
    while len(q) > 0:
        tmp = q.popleft()
        y, x, flag = tmp[0], tmp[1], tmp[2]
        if flag: #불이 퍼진다
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < R and 0 <= nx < C and board[ny][nx] != '#' and visit[ny][nx] != 2:
                    q.append([ny, nx, 1])
                    visit[ny][nx] = 2
        else:
            t = tmp[3]
            if visit[y][x] != 2:
                if y == 0 or y == R - 1 or x == 0 or x == C - 1:
                    return t + 1
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < R and 0 <= nx < C and visit[ny][nx] == 0 and board[ny][nx] != '#':
                        q.append([ny, nx, 0, t + 1])
                        visit[ny][nx] = 1
    return 'IMPOSSIBLE'


if __name__ == '__main__':
    main()
