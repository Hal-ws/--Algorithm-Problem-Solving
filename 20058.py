import sys
from collections import deque


def main():
    global N, board, dy, dx, visit
    N, Q = map(int, sys.stdin.readline().split())
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    board = []
    visit = [[0 for j in range(pow(2, N))] for i in range(pow(2, N))]
    for i in range(pow(2, N)):
        board.append(list(map(int, sys.stdin.readline().split())))
    spells = list(map(int, sys.stdin.readline().split()))
    for L in spells:
        firestorm(L)
    iceCnt = 0
    maxVol = 0
    for i in range(pow(2, N)):
        for j in range(pow(2, N)):
            if board[i][j] != 0:
                iceCnt += board[i][j]
                if visit[i][j] == 0:
                    tmpVol = bfs([i, j])
                    if maxVol < tmpVol:
                        maxVol = tmpVol
    print(iceCnt)
    print(maxVol)


def firestorm(L):
    global N, board, dy, dx
    for i in range(0, pow(2, N), pow(2, L)):
        for j in range(0, pow(2, N), pow(2, L)):
            rotation([i, j], L)
    meltChk = [[0 for j in range(pow(2, N))] for i in range(pow(2, N))]
    for i in range(pow(2, N)):
        for j in range(pow(2, N)):
            if board[i][j] != 0:
                cnt = 0
                for k in range(4):
                    ny, nx = i + dy[k], j + dx[k]
                    if 0 <= ny < pow(2, N) and 0 <= nx < pow(2, N) and board[ny][nx] != 0:
                        cnt += 1
                if cnt < 3:
                    meltChk[i][j] = 1
    for i in range(pow(2, N)):
        for j in range(pow(2, N)):
            if meltChk[i][j]:
                board[i][j] -= 1


def rotation(pos, L): #좌상 좌표, 격자 구분
    global N, board
    for layer in range(pow(2, L) // 2):
        y, x = pos[0] + layer, pos[1] + layer
        q = deque()
        length = pow(2, L) - 2 * layer
        lu = [y, x]
        ld = [y + length - 1, x]
        ru = [y, x + length - 1]
        rd = [y + length - 1, x + length - 1]
        for j in range(lu[1], ru[1] + 1):
            q.append(board[lu[0]][j])
        for i in range(ru[0] + 1, rd[0] + 1):
            q.append(board[i][rd[1]])
        for j in range(rd[1] - 1, ld[1] - 1, -1):
            q.append(board[rd[0]][j])
        for i in range(ld[0] - 1, lu[0], - 1):
            q.append(board[i][ld[1]])
        for cnt in range(length - 1):
            q.appendleft(q.pop())
        idx = 0
        for j in range(lu[1], ru[1] + 1):
            board[lu[0]][j] = q[idx]
            idx += 1
        for i in range(ru[0] + 1, rd[0] + 1):
            board[i][rd[1]] = q[idx]
            idx += 1
        for j in range(rd[1] - 1, ld[1] - 1, -1):
            board[rd[0]][j] = q[idx]
            idx += 1
        for i in range(ld[0] - 1, lu[0], - 1):
            board[i][ld[1]] = q[idx]
            idx += 1


def bfs(pos):
    global N, board, dy, dx, visit
    q = deque()
    y, x = pos[0], pos[1]
    vol = 1
    q.append([y, x])
    visit[y][x] = 1
    while len(q) > 0:
        y, x = q[0][0], q[0][1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < pow(2, N) and 0 <= nx < pow(2, N) and board[ny][nx] != 0 and visit[ny][nx] == 0:
                vol += 1
                visit[ny][nx] = 1
                q.append([ny, nx])
        q.popleft()
    return vol


if __name__ == '__main__':
    main()
