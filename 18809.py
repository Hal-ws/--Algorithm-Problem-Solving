import sys
from collections import deque
from itertools import combinations


def main():
    global board, dy, dx, liquidPos, N, M
    N, M, G, R = map(int, sys.stdin.readline().split())
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    answer = 0
    tLiquid = 0
    liquidPos = [] # 용액을 뿌릴 수 있는 위치가 idx별로 저장됨
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                tLiquid += 1
                liquidPos.append([i, j])
    liquidIdx = [i for i in range(tLiquid)]
    gCases = list(combinations(liquidIdx, G))
    for gIdxList in gCases:
        rPossible = [] # red의 위치가 될 수 있는 idx를 고름
        for i in range(tLiquid):
            if i not in gIdxList:
                rPossible.append(i)
        rCases = list(combinations(rPossible, R))
        for rIdxList in rCases:
            tmp = bfs(gIdxList, rIdxList)
            if tmp > answer:
                answer = tmp
    print(answer)


def bfs(gIdxList, rIdxList):
    global board, dy, dx, liquidPos, N, M
    visit = [[-1 for j in range(M)] for i in range(N)] # 용액이 퍼진 시간 기록
    color = [[0 for j in range(M)] for i in range(N)] # 어떤 용액이 있는지 기록. G: 1, R: 2, F: 3
    cnt = 0
    q = deque()
    for idx in gIdxList:
        y, x = liquidPos[idx][0], liquidPos[idx][1]
        visit[y][x] = 0
        color[y][x] = 1
        q.append([y, x, 1, 0]) # y, x, color, time 기록
    for idx in rIdxList:
        y, x = liquidPos[idx][0], liquidPos[idx][1]
        visit[y][x] = 0
        color[y][x] = 2
        q.append([y, x, 2, 0])
    while len(q) > 0:
        tmp = q.popleft()
        y, x, liquid, time = tmp[0], tmp[1], tmp[2], tmp[3]
        if color[y][x] == 3: # 이미 꽃이 핀 자리임
            continue
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] != 0: # 호수가 아닌 곳에만 퍼질 수 있음
                if visit[ny][nx] == time + 1 and color[ny][nx] != 3: # 동시에 퍼질 수 있는 곳이고 이미 꽃이 안핌
                    if color[ny][nx] != liquid: # 서로 색깔 다른것끼리 섞임. 꽃이 피므로 더 이상 안퍼지니 q에는 안더함
                        color[ny][nx] = 3
                        cnt += 1
                if visit[ny][nx] == -1: # 아직 용액이 안퍼짐
                    color[ny][nx] = liquid
                    visit[ny][nx] = time + 1
                    q.append([ny, nx, liquid, time + 1])
    return cnt


if __name__ == '__main__':
    main()
