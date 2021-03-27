import sys
from collections import deque


def main():
    global board, visit, N, M, dy, dx, disMatrix, roots
    N, M = map(int, sys.stdin.readline().split())
    board = []
    visit = [[0 for j in range(M)] for i in range(N)]
    connect = []
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    answer = 0
    cnt = 1
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    for i in range(N):
        for j in range(M):
            if board[i][j] and visit[i][j] == 0:
                bfs(i, j, cnt)
                cnt += 1
    disMatrix = [[100 for j in range(cnt)] for i in range(cnt)]
    roots = [i for i in range(cnt)]
    for i in range(N):
        for j in range(M):
            if visit[i][j] != 0:
                getdis(i, j)
    for i in range(cnt):
        for j in range(i + 1, cnt):
            if disMatrix[i][j] != 100:
                connect.append([disMatrix[i][j], i, j])
    connect.sort()
    for path in connect:
        d, node1, node2 = path[0], path[1], path[2]
        root1, root2 = find(node1), find(node2)
        if root1 != root2:
            union(root1, root2)
            answer += d
    std = find(1)
    for node in range(2, cnt):
        if find(node) != std:
            answer = -1
            break
    print(answer)


def bfs(y, x, cnt):
    global board, visit, N, M, dy, dx
    q = deque()
    visit[y][x] = cnt
    q.append([y, x])
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and visit[ny][nx] == 0 and board[ny][nx] == 1:
                visit[ny][nx] = cnt
                q.append([ny, nx])


def getdis(y, x):
    global visit, N, M, disMatrix
    start = visit[y][x]
    d = 0
    for i in range(y - 1, -1, -1):
        if visit[i][x] == start:
            break
        if visit[i][x] != 0:
            end = visit[i][x]
            if d >= 2 and d < disMatrix[start][end]:
                disMatrix[start][end] = d
            break
        d += 1
    d = 0
    for i in range(y + 1, N):
        if visit[i][x] == start:
            break
        if visit[i][x] != 0:
            end = visit[i][x]
            if d >= 2 and d < disMatrix[start][end]:
                disMatrix[start][end] = d
            break
        d += 1
    d = 0
    for j in range(x - 1, -1, -1):
        if visit[y][j] == start:
            break
        if visit[y][j] != 0:
            end = visit[y][j]
            if d >= 2 and d < disMatrix[start][end]:
                disMatrix[start][end] = d
            break
        d += 1
    d = 0
    for j in range(x + 1, M):
        if visit[y][j] == start:
            break
        if visit[y][j] != 0:
            end = visit[y][j]
            if d >= 2 and d < disMatrix[start][end]:
                disMatrix[start][end] = d
            break
        d += 1


def union(node1, node2):
    global roots
    root1, root2 = find(node1), find(node2)
    if root1 != root2:
        roots[node2] = roots[node1]


def find(node):
    global roots
    if roots[node] == node:
        return node
    roots[node] = find(roots[node])
    return roots[node]

if __name__ == '__main__':
    main()
