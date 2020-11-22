import sys
from collections import deque

def main():
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    newboard = [[[0, 0] for i in range(M)] for j in range(N)]
    chk = [[0 for i in range(M)] for j in range(N)]
    cnt = 1 # 몇번째 모양인지 표시
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and chk[i][j] == 0:
                painting(board, [i, j], chk, newboard, cnt, N, M)
                cnt += 1
    ans = 0
    for i in range(N):
        for j in range(M):
            if newboard[i][j][1] == 0:
                temp = getarea(newboard, [i, j], N, M)
                if temp >= ans:
                    ans = temp
    print(ans)


def painting(board, pos, chk, newboard, cnt, N, M):
    q = deque()
    q.append(pos)
    chk[pos[0]][pos[1]] = 1
    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]
    paint = []
    area = 1
    while len(q) > 0:
        for i in range(4):
            if 0 <= q[0][0] + dy[i] < N and 0 <= q[0][1] + dx[i] < M:
                if chk[q[0][0] + dy[i]][q[0][1] + dx[i]] == 0 and board[q[0][0] + dy[i]][q[0][1] + dx[i]] == 1:
                    q.append([q[0][0] + dy[i], q[0][1] + dx[i]])
                    chk[q[0][0] + dy[i]][q[0][1] + dx[i]] = 1
                    area += 1
        paint.append(q.popleft())
    lp = len(paint)
    for i in range(lp):
        newboard[paint[i][0]][paint[i][1]] = [cnt, area]


def getarea(newboard, pos, N, M):
    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]
    areaIdx = [] # 이미 추가된 모양의 index를 더함
    area = 0
    for i in range(4):
        if 0 <= pos[0] + dy[i] < N and 0 <= pos[1] + dx[i] < M:
            if newboard[pos[0] + dy[i]][pos[1] + dx[i]][0] != 0 and newboard[pos[0] + dy[i]][pos[1] + dx[i]][0] not in areaIdx:
                area += newboard[pos[0] + dy[i]][pos[1] + dx[i]][1]
                areaIdx.append(newboard[pos[0] + dy[i]][pos[1] + dx[i]][0])
    return area + 1


if __name__ == "__main__":
    main()
