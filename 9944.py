import sys


def main():
    global ans, dy, dx, visit, N, M
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    t_case = 1
    while 1:
        try:
            N, M = map(int, sys.stdin.readline().split())
            board = []
            ans = -1
            visit = [[0 for j in range(M)] for i in range(N)]
            eCnt = 0 # 빈칸 세줌
            for i in range(N):
                board.append(sys.stdin.readline()[:M])
                for j in range(M):
                    if board[i][j] == '*':
                        visit[i][j] = 1
                    else:
                        eCnt += 1
            for i in range(N):
                for j in range(M):
                    if visit[i][j] == 0:
                        visit[i][j] = 1
                        dfs(i, j, -1, 0, eCnt - 1)
                        visit[i][j] = 0
            print('Case %s: %s' %(t_case, ans))
            t_case += 1
        except:
            break


def dfs(y, x, d, cnt, eCnt):
    global ans, dy, dx, visit, N, M
    if eCnt == 0:
        if ans == -1 or cnt < ans:
            ans = cnt
            return
    if d == -1: # 처음일때
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and visit[ny][nx] == 0 :
                visit[ny][nx] = 1
                dfs(ny, nx, i, 1, eCnt - 1)
                visit[ny][nx] = 0
    else: #처음이 아닐때
        ny, nx = y + dy[d], x + dx[d] # 다음 좌표
        if 0 <= ny < N and 0 <= nx < M and visit[ny][nx] == 0: # 진행할 수 있음
            visit[ny][nx] = 1
            dfs(ny, nx, d, cnt, eCnt - 1)
            visit[ny][nx] = 0
        else: #꺾여야됨
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    dfs(ny, nx, i, cnt + 1, eCnt - 1)
                    visit[ny][nx] = 0


if __name__ == '__main__':
    main()
