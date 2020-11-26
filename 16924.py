import sys


def main():
    N, M = map(int, input().split())
    board = []
    for i in range(N):
        board.append(list(map(str, sys.stdin.readline()[:M])))
    startcnt = 0
    marked = [[0 for i in range(M)] for j in range(N)] #그린 부분을 표시
    for i in range(N):
        startcnt += board[i].count("*")
    maxSize = min(N, M) // 2 #board에 넣을 수 있는 십자가의 최대 크기
    pos = [] #그릴 수 있는 십자가 중심의 좌표
    for i in range(1, maxSize + 1):
        drawing(board, i, marked, pos, N, M)
    markingCnt = 0 #총 그린 넓이
    for i in range(N):
        markingCnt += sum(marked[i])
    if markingCnt == startcnt:
        k = len(pos)
        print(k)
        for i in range(k):
            for j in range(3):
                print(pos[i][j], end=' ')
            print()
    else:
        print(-1)


def drawing(board, size, marked, pos, N, M): #board, 십자가의 크기, marking
    for i in range(size, N - size):
        for j in range(size, M - size):
            if chkpos(board, [i, j], size):
                pos.append([i + 1, j + 1, size])
                marking(marked, [i, j], size)


def marking(marked, center, size):
    y, x = center[0], center[1]
    for i in range(y - size, y + size + 1):
        marked[i][x] = 1
    for j in range(x - size, x + size + 1):
        marked[y][j] = 1


def chkpos(board, center, size):# center로 주어진 좌표에 size에 맞는 십자가를 놓을 수 있는지 확인
    y, x = center[0], center[1]
    for i in range(y - size, y + size + 1):
        if board[i][x] != '*':
            return 0
    for j in range(x - size, x + size + 1):
        if board[y][j] != '*':
            return 0
    return 1 # 가능하면 1


if __name__ == "__main__":
    main()
