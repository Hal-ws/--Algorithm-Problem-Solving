from collections import deque
import sys


def main():
    global R, C, board, swan, dy, dx, ans, area
    R, C = map(int, sys.stdin.readline().split())
    swan, board = [],  []
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    day, ans = 0, -1
    area = [[0 for j in range(C)] for i in range(R)]
    for i in range(R):
        board.append(list(sys.stdin.readline()[:C]))
    melt = deque()
    mltCnt = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'L':
                swan.append([i, j])
            if board[i][j] == 'X': #얼음
                for k in range(4):
                    if (0 <= i + dy[k] < R and 0 <= j + dx[k] < C) and (board[i + dy[k]][j + dx[k]] == '.' or board[i + dy[k]][j + dx[k]] == 'L'):
                        melt.append([i, j]) # 다음에 녹을 얼음
                        mltCnt += 1
                        break
            if board[i][j] == '.':
                area[i][j] = 8
    while len(melt) > 0:
        mltIce = melt.popleft()
        area[mltIce[0]][mltIce[1]] = 3
    bfs(swan[0], 1)
    if ans == 0:
        print(0)
        return
    bfs(swan[1], 2)
    for i in range(R):
        print(board[i])
    for i in range(R):
        print(area[i])




def bfs(pos, val):
    global R, C, board, ans, dy, dx, area
    y, x = pos[0], pos[1]
    visit = [[0 for j in range(C)] for i in range(R)]
    q = deque()
    q.append([y, x])
    visit[y][x] = 1
    area[y][x] = val # 백조가 있는 구역 표시
    while len(q) > 0:
        y, x = q[0][0], q[0][1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < R and 0 <= nx < C and visit[ny][nx] == 0:
                if board[ny][nx] == 'L': #같은 구간 안에 백조가 있을때
                    ans = 0
                    return
                elif board[ny][nx] == '.':
                    visit[ny][nx] = 1
                    area[ny][nx] = val
                    q.append([ny, nx])
        q.popleft()
                

if __name__ == '__main__':
    main()
