import sys
from collections import deque


def main():
    N = int(sys.stdin.readline())
    town = []
    for i in range(N):
        town.append(list(sys.stdin.readline()[:N]))
    hBoard = []
    for i in range(N):
        hBoard.append(list(map(int, sys.stdin.readline().split())))
    minH, maxH = 1000001, 0
    KList = []
    for i in range(N):
        for j in range(N):
            if town[i][j] == 'P':
                sY, sX = i, j
            if town[i][j] == 'K':
                KList.append([i, j])
            if hBoard[i][j] <= minH:
                minH = hBoard[i][j]
            if hBoard[i][j] >= maxH:
                maxH = hBoard[i][j]
    left, right = 0, maxH - minH
    ans = right
    while left <= right:
        mid = (left + right) // 2
        visit = [[0 for j in range(N)] for i in range(N)]
        visit[sY][sX] = 1
        print('mid: %s' %mid)
        if dfs(sY, sX, visit, hBoard[sY][sX], hBoard[sY][sX], hBoard, mid, N, KList):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
        visit[sY][sX] = 0
        print('---------------')
    print(ans)


def dfs(y, x, visit, maxH, minH, hBoard, mid, N, KList):
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    flag = 1
    print('y, x, maxH, minH: %s, %s, %s, %s' %(y, x, maxH, minH))
    for i in range(N):
        print(visit[i])
    for pos in KList:
        y, x = pos[0], pos[1]
        if visit[y][x] == 0:
            flag = 0
            break
    if flag:
        return 1
    for i in range(8):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == 0:
            nxtH = hBoard[ny][nx]
            print('ny, nx: %s, %s' %(ny, nx))
            result = 0
            if minH <= nxtH <= maxH:
                visit[ny][nx] = 1
                result = dfs(ny, nx, visit, maxH, minH, hBoard, mid, N, KList)
                visit[ny][nx] = 0
            if maxH < nxtH and nxtH - minH <= mid:
                visit[ny][nx] = 1
                result = dfs(ny, nx, visit, nxtH, minH, hBoard, mid, N, KList)
                visit[ny][nx] = 0
            if nxtH < minH and maxH - nxtH <= mid:
                visit[ny][nx] = 1
                result = dfs(ny, nx, visit, maxH, nxtH, hBoard, mid, N, KList)
                visit[ny][nx] = 0
            if result:
                return 1
    return 0


if __name__ == "__main__":
    main()
