import sys


def main():
    N, K = map(int, sys.stdin.readline().split())
    cBoard = []
    for i in range(N):
        cBoard.append(list(map(int, sys.stdin.readline().split())))
    board = [[[] for j in range(N)] for i in range(N)]
    horseInfos = [[] for i in range(K + 1)]
    for i in range(1, K + 1):
        y, x, d = map(int, sys.stdin.readline().split())
        horseInfos[i] = [y - 1, x - 1, d - 1]
        board[y - 1][x - 1].append(i)
    t = 1
    while t < 1001:
        for hIdx in range(1, K + 1):  # 1부터 K까지 이동
            if move(horseInfos, hIdx, cBoard, board, N):
                print(t)
                return
        t += 1
    print(-1)


def move(horseInfos, hIdx, cBoard, board, N):
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    y, x, d = horseInfos[hIdx][0], horseInfos[hIdx][1], horseInfos[hIdx][2]
    ny, nx = y + dy[d], x + dx[d]
    if 0 <= ny < N and 0 <= nx < N and cBoard[ny][nx] != 2:  # 흰색 아니면 빨간색으로 이동하는 경우
        bIdx = board[y][x].index(hIdx)  # 현재 움직이는 말의 board내 index
        mvList = board[y][x][bIdx:]  # 이 말들을 통째로 이동함
        if cBoard[ny][nx] == 0:  # 흰색으로 이동
            board[ny][nx] += mvList
        else:  # 빨간색으로 이동
            board[ny][nx] += reversed(mvList)
        board[y][x] = board[y][x][:bIdx]
        for h in mvList:
            horseInfos[h][0], horseInfos[h][1] = ny, nx  # 말의 위치 다 변경
    else:  # 파란색으로 이동하는 경우
        if d == 0 or d == 2:
            d = d + 1
        else:
            d = d - 1
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < N and 0 <= nx < N and cBoard[ny][nx] != 2:  # 흰색 아니면 빨간색으로 이동
            bIdx = board[y][x].index(hIdx)
            mvList = board[y][x][bIdx:]
            if cBoard[ny][nx] == 0:
                board[ny][nx] += mvList
            else:
                board[ny][nx] += reversed(mvList)
            board[y][x] = board[y][x][:bIdx]
            for h in mvList:
                horseInfos[h][0], horseInfos[h][1] = ny, nx
            horseInfos[hIdx][2] = d
        else:  # 안움직이고 끝남
            horseInfos[hIdx][2] = d
            return 0
    if len(board[ny][nx]) >= 4:
        return 1
    return 0


if __name__ == "__main__":
    main()
