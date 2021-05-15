import sys


def main():
    global N, ans, dy, dx, pList
    N, a, b, c, d = map(int, sys.stdin.readline().split())
    ans = 0
    pList = [a / 100, b / 100, c / 100, d / 100] # 확률 list
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    visit = [[0 for j in range(2 * N + 1)] for i in range(2 * N + 1)]
    visit[N][N] = 1
    y, x = N, N
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        visit[ny][nx] = 1
        dfs(1, pList[i], visit, ny, nx)
        visit[ny][nx] = 0
    print(ans)


def dfs(cnt, p, visit, y, x): # 현재값, 확률, 방문표시, 현재위치
    global N, ans, dy, dx, pList
    if cnt == N: # N번 이동 끝남
        ans += p
        return
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if visit[ny][nx] == 0:
            visit[ny][nx] = 1
            dfs(cnt + 1, p * pList[i], visit, ny, nx)
            visit[ny][nx] = 0


if __name__ == '__main__':
    main()
