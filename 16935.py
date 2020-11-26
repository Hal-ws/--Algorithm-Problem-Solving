import sys
from collections import deque


def main():
    N, M, R = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    operations = list(map(int, sys.stdin.readline().split())) # R번 연산함
    for i in range(R):
        board, N, M = masteroperation(board, N, M, operations[i])
    for j in range(N):
        for k in range(M):
            print(board[j][k], end=' ')
        print()



def masteroperation(board, N, M, idx): # idx번 operation을 수행
    if idx == 1: #상하반전 operation
        board, N, M = verticalreverse(board, N, M)
    if idx == 2: #좌우반전
        board, N, M = horizontalreverse(board, N, M)
    if idx == 3: #오른쪽 90도 회전
        board, N, M = cwrotation(board, N, M)
    if idx == 4:
        board, N, M = cwrotation(board, N, M)
        board, N, M = cwrotation(board, N, M)
        board, N, M = cwrotation(board, N, M)
    if idx == 5:
        board, N, M = groupmove(board, N, M)
    if idx == 6:
        board, N, M = groupmove(board, N, M)
        board, N, M = groupmove(board, N, M)
        board, N, M = groupmove(board, N, M)
    return board, N, M


def verticalreverse(board, N, M): #1번
    for j in range(M):
        for i in range(N // 2):
            board[i][j], board[N - i - 1][j] = board[N - i - 1][j], board[i][j]
    return board, N, M


def horizontalreverse(board, N, M): #2번
    for i in range(N):
        for j in range(M // 2):
            board[i][j], board[i][M - j - 1] = board[i][M - j - 1], board[i][j]
    return board, N, M

def cwrotation(board, N, M): #3번
    newboard = [[0 for i in range(N)] for j in range(M)]
    luy, lux = 0, 0
    rdy, rdx = N - 1, M - 1
    while luy < rdy and lux < rdx:
        q = deque()
        for j in range(lux, rdx + 1):
            q.append(board[luy][j])
        for i in range(luy + 1, rdy + 1):
            q.append(board[i][rdx])
        for j in range(rdx - 1, lux - 1, -1):
            q.append(board[rdy][j])
        for i in range(rdy - 1, luy, -1):
            q.append(board[i][lux])
        ruy, rux = luy, N - 1 - luy
        ldy, ldx = M - 1 - luy, luy
        for i in range(ruy, ldy + 1):
            newboard[i][rux] = q.popleft()
        for j in range(rux - 1, ldx - 1, - 1):
            newboard[ldy][j] = q.popleft()
        for i in range(ldy - 1, ruy - 1, -1):
            newboard[i][ldx] = q.popleft()
        for j in range(ldx + 1, rux):
            newboard[ruy][j] = q.popleft()
        luy += 1
        lux += 1
        rdy -= 1
        rdx -= 1
    return newboard, M, N


def groupmove(board, N, M): #5번
    newboard = []
    group1, group2, group3, group4 = [], [], [], []
    for i in range(N // 2):
        group1.append(board[i][:(M // 2)])
        group2.append(board[i][(M // 2):])
    for i in range(N // 2, N):
        group4.append(board[i][:M // 2])
        group3.append(board[i][M // 2:])
    for i in range(N // 2):
        newboard.append(group4[i] + group1[i])
    for i in range(N // 2):
        newboard.append(group3[i] + group2[i])
    return newboard, N, M


if __name__ == "__main__":
    main()
