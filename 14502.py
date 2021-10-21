import sys
from itertools import combinations
from copy import deepcopy
from collections import deque


def main():
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    emptyList = []
    virusList = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                emptyList.append([i, j])
            if board[i][j] == 2:
                virusList.append([i, j])
    cases = list(combinations(emptyList, 3))
    ans = 0
    for case in cases:
        newBoard = deepcopy(board)
        ans = max(ans, getArea(newBoard, virusList, case, N, M))
    print(ans)


def getArea(board, virusList, walls, N, M):
    result = 0
    for pos in walls:
        board[pos[0]][pos[1]] = 1
    q = deque()
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for vPos in virusList:
        q.append(vPos)
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 0:
                board[ny][nx] = 2
                q.append([ny, nx])
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                result += 1
    return result


if __name__ == "__main__":
    main()
