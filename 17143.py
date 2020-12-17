import sys


def main():
    global  R, C, M
    R, C, M = map(int, sys.stdin.readline().split())
    sharks = []
    board = [[[] for j in range(C)] for i in range(R)]
    for i in range(M):
        r, c, s, d, z = map(int, sys.stdin.readline().split())
        board[r - 1][c - 1].append([z, i]) # 상어의 크기와 상어idx 저장
        sharks.append([r - 1, c - 1, s, d, z]) #0번상어부터 m - 1번 상어까지 정보 저장
    ans = 0
    print(sharks)
    for j in range(C):
        for i in range(R):
            print(board[i])
        ans += fishing(j, board, sharks)
        print(sharks)
        for i in range(R):
            print(board[i])
        for i in range(M):
            if sharks[i] != [None]: #i번 상어가 안잡아먹혔음(board에 남아있음)
                moving(i, sharks, board) #i번 상어를 움직임
        for i in range(M): # 상어가 다 움직인후 겹치는 상어 제거
            if sharks[i] != [None]:
                y, x = sharks[i][0], sharks[i][1] # 상어의 위치 y, x에 저장
                if len(board[y][x]) > 1: #board의 y, x칸에 상어가 1개 이상 있음
                    board[y][x].sort(reverse=True)
                    for k in range(1, len(board[y][x])):#
                        delShark = board[y][x][k] #삭제될 상어의 정보
                        delIdx = delShark[1] #삭제할 상어의 idx
                        sharks[delIdx] = [None] #
                    board[y][x] = [board[y][x][0]] # 제일 큰 상어만 남김
        print('ans: %s' %ans)
        print('--------------------------')
    print(ans)


def fishing(x, board, sharks):
    global R
    cnt = 0
    idx = -1
    for i in range(R):
        if board[i][x] != []:
            idx = board[i][x][0][1]
            cnt = board[i][x][0][0]
            board[i][x] = []
            break
    if idx >= 0:
        print('idx: %s' %idx)
        sharks[idx] = [None]
    return cnt


def moving(a, sharks, board): # 상어 a가 움직임
    print('move!')
    if sharks[a][3] == 1:
        up(a, sharks[a][0], sharks[a][1], sharks, board, sharks[a][2])
    if sharks[a][3] == 2:
        down(a, sharks[a][0], sharks[a][1], sharks, board, sharks[a][2])
    if sharks[a][3] == 3:
        right(a, sharks[a][0], sharks[a][1], sharks, board, sharks[a][2])
    if sharks[a][3] == 4:
        left(a, sharks[a][0], sharks[a][1], sharks, board, sharks[a][2])



if __name__ == '__main__':
    main()
