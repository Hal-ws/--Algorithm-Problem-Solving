import sys


def main():
    global N, M, k, board, smells, sharks, mvOrder, dy, dx, livingSharks
    N, M, k = map(int, sys.stdin.readline().split())
    board = [[0 for j in range(N)] for i in range(N)]
    smells = [[[0, 0] for j in range(N)] for i in range(N)]
    sharks = [[0, 0, 0] for j in range(M + 1)] #y좌표, x좌표, 방향
    sharks[0] = None
    mvOrder = [[None] for j in range(M + 1)]
    livingSharks = M
    dy, dx = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
    for i in range(N):
        tmp = list(map(int, sys.stdin.readline().split()))
        for j in range(N):
            board[i][j] = tmp[j]
            if board[i][j] != 0: # 상어가 있을때
                sIdx = board[i][j]
                sharks[sIdx][0], sharks[sIdx][1] = i, j
                smells[i][j][0] = sIdx
                smells[i][j][1] = k
    sDir = list(map(int, sys.stdin.readline().split()))
    for i in range(M):
        d = sDir[i]
        sIdx = i + 1
        sharks[sIdx][2] = d
    for i in range(1, M + 1):
        for j in range(4):
            tmp = list(map(int, sys.stdin.readline().split()))
            mvOrder[i].append(tmp)
    t = 1
    while t <= 1000:
        board = move()
        for i in range(N):
            for j in range(N):
                if smells[i][j][1] > 1:
                    smells[i][j][1] -= 1
                elif smells[i][j][1] == 1:
                    smells[i][j] = [0, 0]
        for sIdx in range(1, M + 1):
            if sharks[sIdx] != None: #안잡아먹혔으면 지금 칸에 냄새 퍼뜨림
                y, x = sharks[sIdx][0], sharks[sIdx][1]
                smells[y][x] = [sIdx, k]
        if livingSharks == 1:
            print(t)
            return
        t += 1
    print(-1)


def move():
    global N, M, k, board, smells, sharks, mvOrder, dy, dx, livingSharks
    nxtBoard = [[0 for j in range(N)] for i in range(N)]
    for sIdx in range(1, M + 1):
        if sharks[sIdx] != None:
            y, x, d = sharks[sIdx][0], sharks[sIdx][1], sharks[sIdx][2]
            eflag, mflag = 0, 0
            pList = mvOrder[sIdx][d] # 현재 방향에서의 탐색 우선순위
            for i in pList:
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if smells[ny][nx] == [0, 0]: # 빈칸일때
                        eflag = 1
                        ny1, nx1, nd1 = ny, nx, i
                        break
                    if smells[ny][nx][0] == sIdx: # 자기자신일때
                        if mflag == 0:
                            mflag = 1
                            ny2, nx2, nd2 = ny, nx, i
            if eflag:
                ny, nx, nd = ny1, nx1, nd1
            elif mflag:
                ny, nx, nd = ny2, nx2, nd2
            sharks[sIdx] = [ny, nx, nd]
            if nxtBoard[ny][nx] == 0:
                nxtBoard[ny][nx] = sIdx
            else:
                bIdx = nxtBoard[ny][nx]
                if sIdx < bIdx:
                    sharks[bIdx] = None
                else:
                    sharks[sIdx] = None
                livingSharks -= 1
    return nxtBoard


if __name__ == '__main__':
    main()
