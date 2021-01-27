import sys
from collections import deque
from copy import deepcopy


def main():
    global board, target, start
    board = []
    target = [['1', '2', '3'],
              ['4', '5', '6'],
              ['7', '8', '0']]
    start = [[0 for j in range(3)] for i in range(3)]
    for i in range(3):
        board.append(list(map(str, sys.stdin.readline().split())))
    for i in range(3):
        for j in range(3):
            if board[i][j] == '0':
                hole = [i, j]
    print(bfs(hole))


def bfs(hole):
    global board, target
    q = deque()
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    visit = set()
    visit.add(board[0][0] + board[0][1] + board[0][2]
              + board[1][0] + board[1][1] + board[1][2]
              + board[2][0] + board[2][1] + board[2][2])
    q.append([hole, board, 0]) # hole 위치, board 좌표,
    while len(q) > 0:
        hole = q[0][0]
        board = q[0][1]
        y, x, cnt = hole[0], hole[1], q[0][2]
        if board == target:
            return cnt
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 3 and 0 <= nx < 3: # 교환 가능할때
                board[y][x], board[ny][nx] = board[ny][nx], board[y][x] #교체
                chk = board[0][0] + board[0][1] + board[0][2]\
                      + board[1][0] + board[1][1] + board[1][2]\
                      + board[2][0] + board[2][1] + board[2][2]
                if chk not in visit: # 아직 시도 안한 case일때
                    nBoard = deepcopy(board)
                    visit.add(chk)
                    q.append([[ny, nx], nBoard, cnt + 1])
                board[y][x], board[ny][nx] = board[ny][nx], board[y][x] #원복
        q.popleft()
    return -1


if __name__ == '__main__':
    main()
