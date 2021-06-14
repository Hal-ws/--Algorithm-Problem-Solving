import sys
from _collections import deque


def main():
    R1, C1 = map(int, sys.stdin.readline().split())
    R2, C2 = map(int, sys.stdin.readline().split())
    print(bfs([R2, C2], [R1, C1]))


def bfs(king, sang):
    board = [[0 for j in range(9)] for i in range(10)]
    visit = [[0 for j in range(9)] for i in range(10)]
    visit[sang[0]][sang[1]] = 1
    q = deque()
    board[king[0]][king[1]] = 'K'
    dy = [-3, -3, -2, 2, -2, 2, 3, 3]
    dx = [-2, 2, -3, -3, 3, 3, -2, 2]
    q.append([sang[0], sang[1], 0])
    while len(q) > 0:
        tmp = q.popleft()
        y, x, cnt = tmp[0], tmp[1], tmp[2]
        if board[y][x] == 'K':
            return cnt
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 10 and 0 <= nx < 9 and visit[ny][nx] == 0:
                if i == 0 and board[y - 1][x] == board[y - 2][x - 1] == 0:
                    visit[ny][nx] = 1
                    q.append([ny, nx, cnt + 1])
                if i == 1 and board[y - 1][x] == board[y - 2][x + 1] == 0:
                    visit[ny][nx] = 1
                    q.append([ny, nx, cnt + 1])
                if i == 2 and board[y][x - 1] == board[y - 1][x - 2] == 0:
                    visit[ny][nx] = 1
                    q.append([ny, nx, cnt + 1])
                if i == 3 and board[y][x - 1] == board[y + 1][x - 2] == 0:
                    visit[ny][nx] = 1
                    q.append([ny, nx, cnt + 1])
                if i == 4 and board[y][x + 1] == board[y - 1][x + 2] == 0:
                    visit[ny][nx] = 1
                    q.append([ny, nx, cnt + 1])
                if i == 5 and board[y][x + 1] == board[y + 1][x + 2] == 0:
                    visit[ny][nx] = 1
                    q.append([ny, nx, cnt + 1])
                if i == 6 and board[y + 1][x] == board[y + 2][x - 1] == 0:
                    visit[ny][nx] = 1
                    q.append([ny, nx, cnt + 1])
                if i == 7 and board[y + 1][x] == board[y + 2][x + 1] == 0:
                    visit[ny][nx] = 1
                    q.append([ny, nx, cnt + 1])
    return -1


if __name__ == '__main__':
    main()
