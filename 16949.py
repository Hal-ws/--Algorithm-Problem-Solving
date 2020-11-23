import sys
from collections import deque


def main():
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline()[:M])))
    diso = [[0 for i in range(M)] for j in range(N)] # 원점으로부터의 거리
    dise = [[0 for i in range(M)] for j in range(N)] # 끝점으로부터의 거리
    bfs(diso, board, [0, 0], N, M)
    bfs(dise, board, [N - 1, M - 1], N, M)
    ans = 100000000
    if diso[N - 1][M - 1] != 0:
        ans = diso[N - 1][M - 1]
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                temp = getans(board, diso, dise, [i, j], N, M)
                if temp < ans:
                    ans = temp
    if ans == 100000000:
        print(-1)
    else:
        print(ans)


def bfs(distance, board, pos, N, M):
    q = deque()
    q.append(pos)
    distance[pos[0]][pos[1]] = 1
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]
    while len(q) > 0:
        for i in range(4):
            y = q[0][0] + dy[i]
            x = q[0][1] + dx[i]
            if 0 <= y < N and 0 <= x < M and distance[y][x] == 0 and board[y][x] == 0:
                q.append([y, x])
                distance[y][x] = distance[q[0][0]][q[0][1]] + 1
        q.popleft()


def getans(board, diso, dise, pos, N, M):
    y, x= pos[0], pos[1]
    dis = 100000000
    if 0 <= y - 1 and y + 1 < N:
        if board[y - 1][x] == 0 and board[y + 1][x] == 0: #상하로 비었을때 연결
            dis = connecting(diso, dise, [y - 1, x], [y + 1, x], dis)
    if 0 <= x - 1 and x + 1 < M:
        if board[y][x - 1] == 0 and board[y][x + 1] == 0:
            dis = connecting(diso, dise, [y, x - 1], [y, x + 1], dis)
    if 1 <= y and 1 <= x:
        if board[y - 1][x] == 0 and board[y][x - 1] == 0:
            dis = connecting(diso, dise, [y - 1, x], [y, x - 1], dis)
    if 1 <= y and x < M - 1:
        if board[y - 1][x] == 0 and board[y][x + 1] == 0:
            dis = connecting(diso, dise, [y - 1, x], [y, x + 1], dis)
    if y < N - 1 and 1 <= x:
        if board[y + 1][x] == 0 and board[y][x - 1] == 0:
            dis = connecting(diso, dise, [y + 1, x], [y, x - 1], dis)
    if y < N - 1 and x < M - 1:
        if board[y + 1][x] == 0 and board[y][x + 1] == 0:
            dis = connecting(diso, dise, [y + 1, x], [y, x + 1], dis)
    return dis


def connecting(diso, dise, pos1, pos2, dis):
    temp1, temp2 = 100000000, 100000000
    if diso[pos1[0]][pos1[1]] != 0 and dise[pos2[0]][pos2[1]] != 0:
        temp1 = diso[pos1[0]][pos1[1]] + dise[pos2[0]][pos2[1]] + 1
    if diso[pos2[0]][pos2[1]] != 0 and dise[pos1[0]][pos1[1]] != 0:
        temp2 = diso[pos2[0]][pos2[1]] + dise[pos1[0]][pos1[1]] + 1
    tempmin = min(temp1, temp2)
    if tempmin < dis:
        return tempmin
    else:
        return dis


if __name__ == "__main__":
    main()
