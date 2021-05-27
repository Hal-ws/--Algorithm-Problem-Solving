import sys
from collections import deque


def main():
    h, w = map(int, sys.stdin.readline().split())
    ans = 0
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    board = [list('.' * (w + 2))]
    for i in range(h):
        board.append(['.'] + list(sys.stdin.readline()[:w]) + ['.'])
    board.append(list('.' * (w + 2)))
    visit = [[0 for j in range(w + 2)] for i in range(h + 2)]
    visit[0][0] = 1
    q = deque()
    q.append([0, 0])
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < h + 2 and 0 <= nx < w + 2 and visit[ny][nx] == 0 and board[ny][nx] == '.':
                visit[ny][nx] = 1
                q.append([ny, nx])
        for i in range(4, 8):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < h + 2 and 0 <= nx < w + 2 and visit[ny][nx] == 0 and board[ny][nx] == '.':
                if i == 4 and board[y - 1][x] == '\\' and board[y][x - 1] == '\\':
                    visit[ny][nx] = 1
                    q.append([ny, nx])
                if i == 5 and board[y - 1][x] == '/' and board[y][x + 1] == '/':
                    visit[ny][nx] = 1
                    q.append([ny, nx])
                if i == 6 and board[y + 1][x] == '/' and board[y][x - 1] == '/':
                    visit[ny][nx] = 1
                    q.append([ny, nx])
                if i == 7 and board[y + 1][x] == '\\' and board[y][x + 1] == '\\':
                    visit[ny][nx] = 1
                    q.append([ny, nx])
    q = deque()
    flag = 0
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if board[i][j] != '.':
                flag = 1
                q.append([i, j])
                visit[i][j] = 1
                ans += 0.5
                break
        if flag:
            break
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < h + 2 and 0 <= nx < w + 2 and visit[ny][nx] == 0:
                if board[ny][nx] == '.':
                    ans += 1
                    visit[ny][nx] = 1
                    q.append([ny, nx])
                else:
                    ans += 0.5
                    visit[ny][nx] = 1
                    q.append([ny, nx])
    print(int(ans))


if __name__ == '__main__':
    main()
