import sys


def main():
    global N, M, board, ans, dy, dx, visit
    N, M = map(int, sys.stdin.readline().split())
    board = []
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
    visit = [[0 for j in range(M)] for i in range(N)]
    ans = 'No'
    for i in range(N):
        board.append(sys.stdin.readline()[:M])
    for i in range(N):
        for j in range(M):
            visit[i][j] = 1
            dfs([i, j], [i, j], 0, -1)
            visit[i][j] = 0
            if ans == 'Yes':
                print(ans)
                return
    print(ans)


def dfs(start, cur, cnt, v): #시작위치, cur, 꺾은횟수, 기존 진행방향
    global N, M, board, ans, dy, dx, visit
    y, x = cur[0], cur[1]
    if ans == "Yes":
        return
    if v == -1: #시작위치일때
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx] == board[y][x]:
                    dfs(start, [ny, nx], 0, i) #
    else:
        flag = 0
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if board[y][x] == board[ny][nx]:
                    c = dy[v] * dy[i] + dx[v] * dx[i]# cross product
                    if c != -1: #자기자신으로 돌아가면 안됨
                        flag = 1
                        if c == 0: #수직으로 진행. 꺾음
                            if cnt >= 3 and visit[ny][nx] == 1: #3번 이미 꺾고 방문할 곳으로 돌아감
                                ans = 'Yes'
                                return
                            visit[ny][nx] = 1
                            dfs(start, [ny, nx], cnt + 1, i)
                        else:
                            if cnt >= 3 and visit[ny][nx] == 1: #3번 이미 꺾고 방문할 곳으로 돌아감
                                ans = 'Yes'
                                return
                            visit[ny][nx] = 1
                            dfs(start, [ny, nx], cnt, i)
                        visit[ny][nx] = 0
        if flag == 0:
            return


if __name__ == '__main__':
    main()
