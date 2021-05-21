import sys
from collections import deque


def main():
    global N, M, board, dy, dx, connect
    N, M = map(int, sys.stdin.readline().split())
    board = [['*' for j in range(M + 2)]]
    dy = [-1, -1, -1, 0, 1, 0, 1, 1]
    dx = [-1, 0, 1, -1, -1, 1, 1, 0]
    hList = [] #높이 기록
    for i in range(N):
        board.append(list('*' + sys.stdin.readline()[:M] + '*'))
    board.append(['*' for j in range(M + 2)])
    iIdx = 0 # island idx
    connect = []
    q = deque()
    flag = 0
    for i in range(N + 2):
        for j in range(M + 2):
            if board[i][j] == 'x':
                flag = 1
                getIsland([i, j], iIdx)
                connect.append([0, -1]) # idx번째 섬이 포함하고 있는 섬들의 숫자 / idx섬을 포함하는 섬의 idx
                hList.append(-1)
                iIdx += 1
    if flag:
        topdown()
        for iIdx in range(len(connect)):
            if connect[iIdx][0] == 0: # 어떤 섬도 포함 안할때
                hList[iIdx] = 0
                q.append(iIdx)
        while len(q) > 0:
            iIdx = q.popleft() # 현재 island의 idx
            if connect[iIdx][1] != None:# 어떤 섬에 포함되어있을때
                nIdx = connect[iIdx][1]
                connect[nIdx][0] -= 1
                if hList[nIdx] < hList[iIdx] + 1: # 높이 조정
                    hList[nIdx] = hList[iIdx] + 1
                if connect[nIdx][0] == 0:
                    q.append(nIdx)
        ansList = [0] * (max(hList) + 1)
        for h in hList:
            ansList[h] += 1
        for h in ansList:
            print(h, end=' ')
    else:
        print(-1)


def getIsland(pos, iIdx):
    global N, M, board, dy, dx
    y, x = pos[0], pos[1]
    visit = [[0 for j in range(M + 2)] for i in range(N + 2)]
    visit[y][x] = 1
    q = deque()
    q.append([y, x])
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        board[y][x] = iIdx
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N + 2 and 0 <= nx < M + 2 and visit[ny][nx] == 0 and board[ny][nx] == 'x':
                q.append([ny, nx])
                visit[ny][nx] = 1


def topdown(): # 해당 위치에서 같은 섬들 or 빈칸으로 이동해가며 밖으로 나감
    global N, M, board, dy, dx, connect
    visit = [[0 for j in range(M + 2)] for i in range(N + 2)]
    q = deque()
    islandQ = deque()
    visit[0][0] = 1
    q.append([0, 0]) # 바깥쪽부터 돌면서 포함되지 않은 섬을 찾음
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        for i in range(1, 8, 2):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N + 2 and 0 <= nx < M + 2 and visit[ny][nx] == 0:
                if board[ny][nx] == '.' or board[ny][nx] == '*':
                    visit[ny][nx] = 1
                    q.append([ny, nx])
                else: # 섬과 만남
                    iIdx = board[ny][nx]
                    if connect[iIdx][1] == -1:
                        connect[iIdx][1] = None
                        islandQ.append([iIdx, ny, nx])
    while len(islandQ) > 0:
        tmp = islandQ.popleft()
        iIdx, y, x = tmp[0], tmp[1], tmp[2]
        visit[y][x] = 1
        q = deque()
        q.append([y, x])
        while len(q) > 0:
            tmp = q.popleft()
            y, x = tmp[0], tmp[1]
            if board[y][x] == iIdx: # 섬 위에 있을때
                for i in range(8):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < N + 2 and 0 <= nx < M + 2 and visit[ny][nx] == 0:
                        if board[ny][nx] == iIdx or board[ny][nx] == '.':
                            q.append([ny, nx])
                            visit[ny][nx] = 1
            else: # 점 위에 있을때
                for i in range(1, 8, 2):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < N + 2 and 0 <= nx < M + 2 and visit[ny][nx] == 0:
                        if board[ny][nx] == iIdx or board[ny][nx] == '.':
                            q.append([ny, nx])
                            visit[ny][nx] = 1
                        elif board[ny][nx] != '*': # 다른 섬을 만났을때
                            nIdx = board[ny][nx] # nIdx는 iIdx에 포함되는 섬임
                            if connect[nIdx][1] == -1:
                                connect[nIdx][1] = iIdx
                                connect[iIdx][0] += 1
                                islandQ.append([nIdx, ny, nx])


if __name__ == '__main__':
    main()
