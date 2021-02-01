import sys
from collections import deque


def main():
    global N, M, board, dy, dx
    N, M, T = map(int, sys.stdin.readline().split())
    board = [deque() for i in range(N + 1)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    ans = 0
    for i in range(1,N + 1):
        tmp = list(map(int, sys.stdin.readline().split()))
        for j in range(M):
            board[i].append(tmp[j])
    for t in range(T):
        x, d, k = map(int, sys.stdin.readline().split())
        for layer in range(x, N + 1, x):
            rotating(layer, d, k)
        tmp = erasing()
        flag, average = tmp[0], tmp[1]
        if flag == 0:
            for i in range(1, N + 1):
                for j in range(M):
                    if board[i][j] < average and board[i][j] != 0:
                        board[i][j] += 1
                    elif board[i][j] > average and board[i][j] != 0:
                        board[i][j] -= 1
    for i in range(1, N + 1):
        for j in range(M):
            ans += board[i][j]
    print(ans)


def rotating(layer, d, k):
    global N, M, board
    if d == 0: # 시계방향 k칸 회전
        for t in range(k):
            board[layer].appendleft(board[layer].pop())
    else:
        for t in range(k):
            board[layer].append(board[layer].popleft())


def erasing():
    global N, M, board, dy, dx
    cnt = 0 #0이 아닌 숫자의 갯수(평균 구할때 활용)
    tmpSum = 0
    aflag = 0
    eraseChk = [[0 for j in range(M)] for i in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(M):
            if board[i][j] != 0:
                cnt += 1
                tmpSum += board[i][j]
                flag = 0
                for k in range(4):
                    ny, nx = i + dy[k], j + dx[k]
                    if ny == N + 1:
                        continue
                    if ny == 0:
                        continue
                    if nx == M:
                        continue
                    if board[ny][nx] == board[i][j]:
                        flag = 1 #
                        eraseChk[ny][nx] = 1
                if flag:
                    aflag = 1
                    eraseChk[i][j] = 1
    if cnt > 0:
        average = tmpSum / cnt
    else:
        average = 0
    if aflag:
        for i in range(1, N + 1):
            for j in range(M):
                if eraseChk[i][j]:
                    board[i][j] = 0 # 지움
    return [aflag, average]


if __name__ == '__main__':
    main()
