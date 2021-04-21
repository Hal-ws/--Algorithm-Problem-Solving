import sys
from copy import deepcopy
from collections import deque


def main():
    global N, M
    N, M = map(int, sys.stdin.readline().split())
    A, B = [], []
    for i in range(4):
        x, y = map(int, sys.stdin.readline().split())
        if i < 2:
            A.append([y, x])
        else:
            B.append([y, x])
    result1 = bfs(A, B)
    result2 = bfs(B, A)
    if result1 == None and result2 == None:
        print('IMPOSSIBLE')
    elif result1 == None and result2 != None:
        print(result2)
    elif result1 != None and result2 == None:
        print(result1)
    else:
        print(min(result1, result2))


def bfs(path1, path2): # path1 먼저, path2 나중
    global N, M
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    visit = [[0 for j in range(N + 1)] for i in range(M + 1)]
    q = deque()
    visit[path1[0][0]][path1[0][1]] = 9
    visit[path1[1][0]][path1[1][1]] = 9
    visit[path2[0][0]][path2[0][1]] = 9
    visit[path2[1][0]][path2[1][1]] = 9
    q.append([path1[0][0], path1[0][1], 0, [[path1[0][0], path1[0][1]]]])
    flag1, flag2 = 0, 0
    l1, l2 = None, None
    while len(q) > 0:
        tmp = q.popleft()
        y, x, cnt, path = tmp[0], tmp[1], tmp[2], tmp[3]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < M + 1 and 0 <= nx < N + 1:
                nPath = deepcopy(path)
                nPath.append([ny, nx])
                if visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    q.append([ny, nx, cnt + 1, nPath])
                if visit[ny][nx] == 9:
                    if ny == path1[1][0] and nx == path1[1][1]:
                        flag1 = 1
                        l1 = cnt + 1
                        APath = nPath
                        break
        if flag1:
            for p in APath:
                y, x = p[0], p[1]
                visit[y][x] = 9
            break
    for i in range(M + 1):
        for j in range(N + 1):
            if visit[i][j] == 1:
                visit[i][j] = 0
    q = deque()
    q.append([path2[0][0], path2[0][1], 0])
    while len(q) > 0:
        tmp = q.popleft()
        y, x, cnt = tmp[0], tmp[1], tmp[2]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < M + 1 and 0 <= nx < N + 1:
                if visit[ny][nx] == 0:
                    q.append([ny, nx, cnt + 1])
                    visit[ny][nx] = 1
                elif ny == path2[1][0] and nx == path2[1][1]:
                    flag2 = 1
                    l2 = cnt + 1
                    break
        if flag2:
            break
    if flag1 + flag2 == 2:
        return l1 + l2
    else:
        return None


if __name__ == '__main__':
    main()
