import sys
from collections import deque


def main():
    N = int(sys.stdin.readline())
    town = []
    for i in range(N):
        town.append(list(sys.stdin.readline()[:N]))
    hList = []
    for i in range(N):
        hList.append(list(map(int, sys.stdin.readline().split())))
    minH, maxH = 1000001, 0
    for i in range(N):
        for j in range(N):
            if town[i][j] == 'P':
                sPos = [i, j]
            if hList[i][j] <= minH:
                minH = hList[i][j]
            if hList[i][j] >= maxH:
                maxH = hList[i][j]
    left, right = 0, maxH - minH
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if bfs(sPos, town, hList, mid, N):  # mid의 피로도로 이동가능
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ans)


def bfs(sPos, town, hList, mid, N):
    y, x = sPos[0], sPos[1]
    visit = [[0 for j in range(N)] for i in range(N)]
    visit[y][x] = 1
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    q = deque()
    q.append([y, x])
    minH, maxH = 1000001, 0
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        curH = hList[y][x]
        flag = 1
        if curH > maxH:
            if curH - minH > mid:
                visit[y][x] = -1
                flag = 0
        if curH <= minH:
            if maxH - curH > mid:
                visit[y][x] = -1
                flag = 0
        if flag:
            if curH >= maxH:
                maxH = curH
            if curH <= minH:
                minH = curH
            for i in range(8):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == 0:
                    q.append([ny, nx])
                    visit[ny][nx] = 1
    for i in range(N):
        for j in range(N):
            if town[i][j] == 'K' and visit[i][j] != 1:
                return 0
    return 1


if __name__ == "__main__":
    main()
