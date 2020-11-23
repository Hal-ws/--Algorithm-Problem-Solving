import sys
from _collections import deque


def main():
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline()[:M])))
    chk = [[0 for i in range(M)] for j in range(N)]
    newboard = [[[0, 0] for i in range(M)] for j in range(N)]
    idx = 1
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 and chk[i][j] == 0:
                bfs(board, newboard, chk, idx, [i, j], N, M)
                idx += 1
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                board[i][j] = getans(newboard, [i, j], N, M) % 10
    for i in range(N):
        for j in range(M):
            print(board[i][j], end='')
        print()
    return 0


def bfs(board, newboard, chk, idx, pos, N, M):
    q = deque()
    q.append(pos)
    chk[pos[0]][pos[1]] = 1
    dy = [-1, 0, 0, 1]
    dx = [0, 1, -1, 0]
    areaq = [pos]
    area = 1
    while len(q) > 0:
        for i in range(4):
            y = q[0][0] + dy[i]
            x = q[0][1] + dx[i]
            if 0 <= y < N and 0 <= x < M and board[y][x] == 0 and chk[y][x] == 0:
                q.append([y, x])
                chk[y][x] = 1
                area += 1
        areaq.append(q.popleft())
    la = len(areaq)
    for i in range(la):
        newboard[areaq[i][0]][areaq[i][1]] = [idx, area]


def getans(newboard, pos, N, M):
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]
    idxList = []
    ans = 1
    for i in range(4):
        y = pos[0] + dy[i]
        x = pos[1] + dx[i]
        if 0 <= y < N and 0 <= x < M and newboard[y][x][0] not in idxList and newboard[y][x][1] != 0:
            idxList.append(newboard[y][x][0])
            ans += newboard[y][x][1]
    return ans


if __name__ == "__main__":
    main()
