import sys
from itertools import combinations
from collections import deque


def main():
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    viruses = []
    vn = 0 # virus number
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                viruses.append([vn, i, j])
                board[i][j] = "*" # 시간 표시할거니까 숫자 변경. 바이러스
                vn += 1
            if board[i][j] == 0:
                board[i][j] = "O" # 빈공간
            if board[i][j] == 1:
                board[i][j] = "W" # wall
    cases = list(combinations(viruses, M)) # 바이러스 중 M개를 뽑음
    timeRecode = [] #각각의 virus별로 혼자 active 됐을때 걸리는 시간
    for i in range(len(viruses)): # 0번 바이러스부터 마지막 바이러스까지 혼자 움직일때의 시간 기록
        timeRecode.append(bfs(board, [viruses[i][1], viruses[i][2]], N))
    minTime = 9999999999999
    flag = 0 #
    for case in cases:
        tmp = getTime(board, timeRecode, case, N)
        if tmp != -1: # 이 case에 대해서 전 실험실에 바이러스 전파 가능
            flag = 1
            if tmp <= minTime:
                minTime = tmp
    if flag:
        print(minTime)
    else: # 끝까지 -1로 유지. 모든 case에 대해서 바이러스 전파가 불가능함
        print(-1)

def bfs(board, pos, N):
    y, x = pos[0], pos[1]
    q = deque()
    timeboard = [[-1 for j in range(N)] for i in range(N)] #도착한 시간을 기록. -1은 도착 안했다는 뜻
    visitChk = [[0 for j in range(N)] for i in range(N)]
    visitChk[y][x] = 1
    q.append([y, x, 0]) #전파 위치 출력
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while len(q) > 0:
        curY = q[0][0]
        curX = q[0][1]
        curT = q[0][2]
        for i in range(4):
            ny = curY + dy[i]
            nx = curX + dx[i]
            if 0 <= ny < N and 0 <= nx < N and visitChk[ny][nx] == 0:
                if board[ny][nx] == "O" or board[ny][nx] == "*":
                    q.append([ny, nx, curT + 1])
                    visitChk[ny][nx] = 1
        timeboard[curY][curX] = curT
        q.popleft()
    return timeboard


def getTime(board, timeRecode, case, N): # 각 case에 대한 완전전파시간 찾으면 시간 리턴. 그런데 전파 불가능하면 -1리턴
    time = 0
    result = [[0 for j in range(N)] for i in range(N)] # result 에 기록된 최대 시간을 찾아야됨
    for i in range(N):
        for j in range(N):
            if board[i][j] == "O": # 바이러스 전파가능한 지역
                minTime = 9999999999999 # 지역에 도착할때 걸리는 최소시간 확인
                arriveFlag = 0 #각 위치에 대해서 도착할 수 있는지 확인
                for virus in case: # virus에 따른 timeRecode의 좌표값 구함
                    virusIdx = virus[0]
                    if timeRecode[virusIdx][i][j] != - 1 and timeRecode[virusIdx][i][j] <= minTime:
                        minTime = timeRecode[virusIdx][i][j]
                        arriveFlag = 1
                if arriveFlag == 0: #도착 불가능함. 얘는 도착안됨
                    return -1
                result[i][j] = minTime
                if time <= result[i][j]:
                    time = result[i][j]
    return time


if __name__ == "__main__":
    main()
