import sys
from collections import deque


def main():
    global w, h, board, dy, dx
    T = int(sys.stdin.readline())
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for i in range(T):
        w, h = map(int, sys.stdin.readline().split())
        board = []
        for j in range(h):
            board.append(list(sys.stdin.readline()[:w]))
        fire = deque()
        for j in range(h):
            for k in range(w):
                if board[j][k] == '@':
                    sang = [j, k]
                if board[j][k] == '*':
                    fire.append([j, k, 0])
        bfs(sang, fire)


def bfs(pos, fire):
    global w, h, board, dy, dx
    visit = [[0 for j in range(w)] for i in range(h)]
    ys, xs = pos[0], pos[1] #상근이 위치
    if ys == 0 or ys == h - 1 or xs == 0 or xs == w - 1:
        print(1)
        return
    visit[ys][xs] = 1
    q = deque()
    q.append([ys, xs, 0])
    endflag = 0
    while 1:
        if len(fire) > 0:
            iniFire = fire[0][2]
            while len(fire) > 0:
                y, x, d = fire[0][0], fire[0][1], fire[0][2]
                if d > iniFire: #한칸 이상 움직였을때
                    break
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < h and 0 <= nx < w and board[ny][nx] == '.':
                        board[ny][nx] = '*'
                        fire.append([ny, nx, d + 1])
                fire.popleft()
        if len(q) > 0:
            iniSang = q[0][2]
            while len(q) > 0:
                ys, xs, d = q[0][0], q[0][1], q[0][2]
                if ys == 0 or ys == h - 1 or xs == 0 or xs == w - 1:
                    endflag = 1
                    ans = d + 1
                    break
                if d > iniSang:
                    break
                for i in range(4):
                    nys, nxs = ys + dy[i], xs + dx[i]
                    if 0 <= nys < h and 0 <= nxs < w and board[nys][nxs] != '*' and board[nys][nxs] != '#' and visit[nys][nxs] == 0:
                        visit[nys][nxs] = 1
                        q.append([nys, nxs, d + 1])
                q.popleft()
        else:
            break
        if endflag == 1:
            break
    if endflag:
        print(ans)
    else:
        print('IMPOSSIBLE')


if __name__ == '__main__':
    main()
