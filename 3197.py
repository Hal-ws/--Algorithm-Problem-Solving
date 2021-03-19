import sys
from _collections import deque


def main():
    global R, C, dy, dx, board, area, rootIdx
    R, C = map(int, sys.stdin.readline().split())
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    board = []
    swan = []
    area = [[-1 for j in range(C)] for i in range(R)]
    melting = [] # 이 좌표 주변에 있는 얼음덩어리들을 녹임
    rootIdx = [] # 해당 idx의 root를 기록
    for i in range(R):
        board.append(list(sys.stdin.readline()[:C]))
    t, cnt = 0, 0
    for i in range(R):
        for j in range(C):
            if (board[i][j] == '.' or board[i][j] == 'L') and area[i][j] == -1:
                bfs(i, j, cnt)
                rootIdx.append(cnt)
                cnt += 1
            if board[i][j] == 'L':
                swan.append([i, j])
    s1y, s1x, s2y, s2x = swan[0][0], swan[0][1], swan[1][0], swan[1][1]
    if area[s1y][s1x] == area[s1y][s2x]: # 시작부터 같은 곳에 있음
        print(t)
        return
    #녹을 얼음들 리스트 만듬
    for i in range(R):
        for j in range(C):
            if area[i][j] != -1: # 물일때
                for k in range(4):
                    ny, nx = i + dy[k], j + dx[k]
                    if 0 <= ny < R and 0 <= nx < C and area[ny][nx] == -1: # 얼음 발견
                        melting.append([i, j])
    for i in range(R):
        print(area[i])
    print('rootIdx: %s' %rootIdx)
    print('--------------------')
    while 1:
        print('s1 idx, s2 idx: %s, %s' %(area[s1y][s1x], area[s2y][s2x]))
        if findroot(area[s1y][s1x]) == findroot(area[s2y][s2x]):
            print(t)
            break
        nxtMelt = []
        for water in melting: # water 주변의 ice가 녹음
            y, x = water[0], water[1]
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < R and 0 <= nx < C:
                    if area[ny][nx] == -1: # 얼음을 녹임
                        area[ny][nx] = area[y][x]
                        nxtMelt.append([ny, nx])
                    elif area[y][x] != area[ny][nx]:
                        idx1, idx2 = area[y][x], area[ny][nx]
                        joint(idx1, idx2)
        for i in range(R):
            print(area[i])
        print('rootIdx: %s' %rootIdx)
        print('-----------------------')
        melting = [nxtMelt[i] for i in range(len(nxtMelt))]
        t += 1


def joint(idx1, idx2):
    global rootIdx
    if rootIdx[idx1] != rootIdx[idx2]: # 서로 다른 그룹일 때
        rootIdx[idx2] = rootIdx[idx1]


def findroot(areaI): # area idx의 root를 구함
    global rootIdx
    if rootIdx[areaI] == areaI:
        return areaI
    rootIdx[areaI] = findroot(rootIdx[areaI])
    return rootIdx[areaI]


def bfs(y, x, cnt):
    global R, C, dy, dx, board, area
    q = deque()
    area[y][x] = cnt
    q.append([y, x])
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < R and 0 <= nx < C and area[ny][nx] == -1 and board[ny][nx] != 'X':
                q.append([ny, nx])
                area[ny][nx] = cnt


if __name__ == '__main__':
    main()
