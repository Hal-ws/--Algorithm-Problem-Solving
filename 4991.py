import sys
from collections import deque
from itertools import permutations


def main():
    global w, h, board, disMatrix, dy, dx
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    while 1:
        w, h = map(int, sys.stdin.readline().split())
        dirtyCnt = 0
        dirty = [None]
        robot = [0, 0]
        board = []
        ans = 0
        flag = 0
        if w == h == 0:
            break
        for i in range(h):
            board.append(list(sys.stdin.readline()[:w]))
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'o':
                    robot[0], robot[1] = i, j
                if board[i][j] == '*':
                    dirty.append([i, j])
                    dirtyCnt += 1
                    board[i][j] = ['*', dirtyCnt]
        disMatrix = [[0 for j in range(dirtyCnt + 1)] for i in range(dirtyCnt + 1)]
        for i in range(dirtyCnt + 1):
            if i == 0:
                bfs(robot, 0)
                if 0 in disMatrix[0][1:]:
                    print(-1)
                    flag = 1
                    break
            else:
                bfs(dirty[i], i)
        if flag:
            continue
        order = [i for i in range(1, dirtyCnt + 1)]
        cases = list(permutations(order, dirtyCnt))
        for case in cases:
            cur = 0
            tmp = 0
            for nIdx in range(dirtyCnt):
                tmp += disMatrix[cur][case[nIdx]]
                cur = case[nIdx]
            if ans == 0:
                ans = tmp
            elif tmp < ans:
                ans = tmp
        print(ans)


def bfs(start, idx):
    global w, h, board, disMatrix
    q = deque()
    visit = [[0 for j in range(w)] for i in range(h)]
    visit[start[0]][start[1]] = 1
    q.append([start[0], start[1], 0])
    while len(q) > 0:
        y, x, d = q[0][0], q[0][1], q[0][2]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < h and 0 <= nx < w and visit[ny][nx] == 0 and board[ny][nx] != 'x':
                visit[ny][nx] = 1
                if board[ny][nx] != '.' and board[ny][nx] != 'o':
                    dIdx = board[ny][nx][1]
                    disMatrix[idx][dIdx] = d + 1
                if board[ny][nx] == 'o':
                    disMatrix[idx][0] = d + 1
                q.append([ny, nx, d + 1])
        q.popleft()


if __name__ == '__main__':
    main()
