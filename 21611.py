import sys


def main():
    board = []
    N, M = map(int, sys.stdin.readline().split())
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    bombBalls = [None, 0, 0, 0]
    posList = trace(N) # idx별 좌표를 기록. 상어의 idx는 0
    answer = 0
    ballList = [0 for i in range(N * N)]
    for idx in range(1, N * N):
        y, x = posList[idx][0], posList[idx][1]
        ballList[idx] = board[y][x]
    for i in range(M):
        blizzard(board, bombBalls, N, posList, ballList)
    for i in range(1, 4):
        answer += (i * bombBalls[i])
    print(answer)


def blizzard(board, bombBalls, N, posList, ballList):
    d, s = map(int, sys.stdin.readline().split())
    sy, sx = N // 2, N // 2
    dy = [0, -1, 1, 0, 0]
    dx = [0, 0, 0, -1, 1]
    for i in range(1, s + 1):
        ny, nx = sy + i * dy[d], sx + i * dx[d]
        board[ny][nx] = 0
    for idx in range(1, N * N):
        y, x = posList[idx][0], posList[idx][1]
        ballList[idx] = board[y][x]
    move(board, N, posList, ballList)
    while 1:
        if bomb(board, N, posList, ballList, bombBalls) == 0:
            break
    transform(board, N, posList, ballList)


def move(board, N, posList, ballList):
    for i in range(1, N * N):
        if ballList[i] != 0:
            mvIdx = -1
            for j in range(i - 1, 0, -1):
                if ballList[j] == 0: # 앞으로 앞당겨준다
                    mvIdx = j
                else:
                    break
            if mvIdx != -1:
                ballList[i], ballList[mvIdx] = ballList[mvIdx], ballList[i]
    for idx in range(1, N * N):
        y, x = posList[idx][0], posList[idx][1]
        board[y][x] = ballList[idx]


def bomb(board, N, posList, ballList, bombBalls): #4개 이상 겹치는거 제거
    flag = 0
    cnt = 1
    std = ballList[1]
    if std != 0:
        for idx in range(2, N * N):
            if ballList[idx] == std:
                cnt += 1
                if cnt == 4:
                    for i in range(4):
                        ballList[idx - i] = 0
                    bombBalls[std] += 4
                    flag = 1
                if cnt > 4:
                    ballList[idx] = 0
                    bombBalls[std] += 1
            elif ballList[idx] != 0:
                cnt = 1
                std = ballList[idx]
        if flag: # 폭발했으니 이동시켜준다
            for idx in range(1, N * N):
                y, x = posList[idx][0], posList[idx][1]
                board[y][x] = ballList[idx]
            move(board, N, posList, ballList)
    return flag


def transform(board, N, posList, ballList):
    nballList = [0]
    std = ballList[1]
    cnt = 1
    if std != 0:
        for idx in range(2, N * N):
            if ballList[idx] == std:
                cnt += 1
                if idx == N * N - 1: # 끝까지 다 갔을때
                    nballList.append(cnt)
                    nballList.append(std)
            else:
                nballList.append(cnt)
                nballList.append(std)
                cnt = 1
                std = ballList[idx]
        l = len(nballList)
        if l < N * N:
            for _ in range(N * N - l):
                nballList.append(0)
        for idx in range(N * N):
            y, x = posList[idx][0], posList[idx][1]
            board[y][x] = nballList[idx]
            ballList[idx] = nballList[idx]


def trace(N): # in일지, out일지 결정하는 flag
    y, x = N // 2, N // 2
    posList = [[None, None] for i in range(N * N)]
    posList[0] = [y, x]
    idx = 1
    d = 1
    while 1:
        for _ in range(d):
            x -= 1
            posList[idx] = [y, x]
            if y == x == 0:
                return posList
            idx += 1
        for _ in range(d):
            y += 1
            posList[idx] = [y, x]
            idx += 1
        d += 1
        for _ in range(d):
            x += 1
            posList[idx] = [y, x]
            idx += 1
        for _ in range(d):
            y -= 1
            posList[idx] = [y, x]
            idx += 1
        d += 1


if __name__ == '__main__':
    main()
