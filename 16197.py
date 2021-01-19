import sys
from collections import deque


def main():
    global N, M, visit, board
    N, M = map(int, sys.stdin.readline().split())
    board = []
    visit = [[[[0 for l in range(20)] for k in range(20)] for j in range(20)] for i in range(20)]
    for i in range(N):
        board.append(list(sys.stdin.readline()[:M]))
    coin = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'o':
                coin.append([i, j])
    ans = bfs(coin)
    print(ans)


def bfs(coin):
    global N, M, visit, board
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    c1, c2 = coin[0], coin[1]
    q = deque()
    visit[c1[0]][c1[1]][c2[0]][c2[1]] = 1
    q.append([c1, c2, 0])
    while len(q) > 0:
        c1, c2, cnt = q[0][0], q[0][1], q[0][2]
        y1, x1, y2, x2 = c1[0], c1[1], c2[0], c2[1]
        if cnt >= 10:
            break
        for i in range(4):
            ny1, nx1 = y1 + dy[i], x1 + dx[i]
            ny2, nx2 = y2 + dy[i], x2 + dx[i]
            flag1, flag2 = 1, 1 # board 안에 있을때 1
            if 0 <= ny1 < N and 0 <= nx1 < M: #밖으로 안나감
                if board[ny1][nx1] != '#': #움직일 수 있을 때
                    nc1 = [ny1, nx1]
                else:
                    nc1 = [y1, x1]
            else: #밖으로 나감
                flag1 = 0
            if 0 <= ny2 < N and 0 <= nx2 < M: # 밖으로 안나감
                if board[ny2][nx2] != '#':
                    nc2 = [ny2, nx2]
                else:
                    nc2 = [y2, x2]
            else: #밖으로 나감
                flag2 = 0
            if flag1 * flag2 == 0 and flag1 + flag2 != 0: #종료조건
                return cnt + 1
            elif flag1 == flag2 == 1:
                if visit[nc1[0]][nc1[1]][nc2[0]][nc2[1]] == 0:
                    visit[nc1[0]][nc1[1]][nc2[0]][nc2[1]] = 1
                    q.append([nc1, nc2, cnt + 1])
        q.popleft()
    return -1


if __name__ == '__main__':
    main()
