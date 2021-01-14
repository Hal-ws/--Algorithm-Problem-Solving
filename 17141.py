import sys
from collections import deque
from itertools import combinations


def main():
    global board, timeBoard, N, M, dy, dx
    N, M = map(int, sys.stdin.readline().split())
    board, timeBoard, virus, vCnt, ans = [], [], [], 0, -1
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                virus.append([i, j])
                vCnt += 1
    cases = list(combinations([i for i in range(vCnt)], M)) #바이러스 number로 만든다
    for i in range(vCnt):
        timeBoard.append(bfs(virus[i]))
    for case in cases:
        tmp = getans(case)
        if tmp != -1: #바이러스 다 퍼뜨림
            if ans == -1 or tmp < ans:
                ans = tmp
    print(ans)


def bfs(pos):
    global board, N, M, dy, dx
    visit = [[0 for j in range(N)] for i in range(N)]
    result = [[-1 for j in range(N)] for i in range(N)]
    y, x = pos[0], pos[1]
    q = deque()
    q.append([y, x, 0])
    visit[y][x] = 1
    result[y][x] = 0
    while len(q) > 0:
        y, x, t = q[0][0], q[0][1], q[0][2]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == 0 and board[ny][nx] != 1:
                visit[ny][nx] = 1
                result[ny][nx] = t + 1
                q.append([ny, nx, t + 1])
        q.popleft()
    return result


def getans(case):
    global board, timeBoard, N, M, virus
    maxTime = -1
    for i in range(N):
        for j in range(N): # [i, j] 좌표 도달 최소시간 구함
            if board[i][j] != 1:
                posTime = -1 # -1일때에는 도착불가
                for k in range(M): #k 번 바이러스 기준 도착시간
                    tmp = timeBoard[case[k]][i][j]
                    if tmp != -1: #도착 가능할때
                        if posTime == -1: #
                            posTime = tmp
                        else:
                            if tmp < posTime:
                                posTime = tmp
                if posTime == -1: #도착불가능한 좌표가 존재함
                    return -1
                else:
                    if maxTime == -1 or maxTime < posTime:
                        maxTime = posTime
    return maxTime


if __name__ == '__main__':
    main()
