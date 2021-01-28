import sys
from collections import deque


def main():
    global N, board, area, dy, dx
    N = int(sys.stdin.readline())
    minDis = 200
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    area = [[0 for j in range(N)] for i in range(N)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    cnt = 1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 and area[i][j] == 0:
                drawarea(i, j, cnt)
                cnt += 1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                flag = 0
                for k in range(4):
                    ny, nx = i + dy[k], j + dx[k]
                    if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0: #섬의 가장자리에 있을때
                        flag = 1
                    if flag:
                        tmp = getnear(i, j, area[i][j])
                        if tmp < minDis:
                            minDis = tmp
    print(minDis)


def getnear(y, x, cnt): #cnt 와 다른 섬을 찾는다
    global N, area, dy, dx
    visit = [[0 for j in range(N)] for i in range(N)]
    q = deque()
    q.append([y, x, 0])
    visit[y][x] = 1
    while len(q) > 0:
        y, x, dis = q[0][0], q[0][1], q[0][2]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and area[ny][nx] != cnt and visit[ny][nx] == 0:
                visit[ny][nx] = 1
                if area[ny][nx] != 0: #새로운 섬 만났을때
                    return dis
                else:
                    q.append([ny, nx, dis + 1])
        q.popleft()
    return 200

def drawarea(y, x, cnt):
    global N, board, area, dy, dx
    q = deque()
    q.append([y, x])
    area[y][x] = cnt
    while len(q) > 0:
        y, x = q[0][0], q[0][1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 1 and area[ny][nx] == 0:
                area[ny][nx] = cnt
                q.append([ny, nx])
        q.popleft()


if __name__ == '__main__':
    main()
