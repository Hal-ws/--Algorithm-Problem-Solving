import sys
from collections import deque


def main():
    global N, M, board, dy, dx, connect, upList, downList, leftList, rightList
    N, M = map(int, sys.stdin.readline().split())
    board = [['*' for j in range(M + 2)]]
    dy = [-1, -1, -1, 0, 1, 0, 1, 1]
    dx = [-1, 0, 1, -1, -1, 1, 1, 0]
    hList = [] #높이 기록
    upList = []
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
                connect.append([0, -1]) # sIdx번째 섬이 포함하고 있는 섬들의 숫자 / sIdx섬을 포함하는 섬의 idx
                hList.append(-1)
                upList.append(51)
                downList.append(-1)
                leftList.append(51)
                rightList.append(-1)
                iIdx += 1
    if flag:
        for i in range(N + 2):
            for j in range(M + 2):
                if board[i][j] != '.' and board[i][j] != '*':
                    if i < upList[board[i][j]]:
                        upList[board[i][j]] = i
                    if i > downList[board[i][j]]:
                        downList[board[i][j]] = i
                    if j <
        print('upList: %s' %upList)
        for i in range(N + 2):
            for j in range(M + 2):
                if board[i][j] != '.' and board[i][j] != '*' and connect[board[i][j]][1] == -1:
                    goout([i, j])
        for iIdx in range(len(connect)):
            if connect[iIdx][0] == 0: # 어떤 섬도 포함 안할때
                hList[iIdx] = 0
                q.append(iIdx)
        print('connect: %s' %connect)
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


def goout(pos): # 해당 위치에서 같은 섬들 or 빈칸으로 이동해가며 밖으로 나감
    global N, M, board, dy, dx, connect, upList, downList, leftList, rightList
    visit = [[0 for j in range(M + 2)] for i in range(N + 2)]
    y, x = pos[0], pos[1]
    sIdx = board[y][x]
    nIdx = None
    visit[y][x] = 1
    q = deque()
    q.append([y, x])
    flag = 0
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        if board[y][x] == '*': # 바깥으로 이동가능
            flag = 1
            break
        if board[y][x] == sIdx: # 8방향 이동가능
            for i in range(8):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N + 2 and 0 <= nx < M + 2 and visit[ny][nx] == 0:
                    if board[ny][nx] == '.' or board[ny][nx] == sIdx or board[ny][nx] == '*':
                        visit[ny][nx] = 1
                        q.append([ny, nx])
        if board[y][x] == '.': # 십자방향으로만 이동가능
            for i in range(1, 8, 2):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N + 2 and 0 <= nx < M + 2 and visit[ny][nx] == 0:
                    if board[ny][nx] == '.' or board[ny][nx] == sIdx or board[ny][nx] == '*':
                        visit[ny][nx] = 1
                        q.append([ny, nx])
                    else:
                        nIdx = board[ny][nx]
    if flag: # 바깥으로 이동가능함
        connect[sIdx][1] = None # sIdx를 포함하는 island가 없음
    else: # 바깥으로 이동 불가. 만나는 다른 점과 포함관계 확인해줘야함
        print('sIdx, nIdx: %s, %s' %(sIdx, nIdx))
        if upList[sIdx] < upList[nIdx]: # nIdx가 sIdx 안에 들어감
            print('%s 가 %s 안에 들어감' %(nIdx, sIdx))
            connect[nIdx][1] = sIdx
            connect[sIdx][0] += 1
        else:
            print('%s가 %s 안에 들어감' %(sIdx, nIdx))
            connect[sIdx][1] = nIdx # nIdx 안에 들어가는 섬임
            connect[nIdx][0] += 1 # nIdx가 포함하는 섬들의 숫자


if __name__ == '__main__':
    main()
