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
                flag = 0
                for k in range(4):
                    ny, nx = i + dy[k], j + dx[k]
                    if 0 <= ny < R and 0 <= nx < C and area[ny][nx] == -1: # 얼음 발견
                        flag = 1
                if flag:
                    melting.append([i, j]) # 가장자리에 있는 얼음들 위치 저장
    while 1:
        if findroot(area[s1y][s1x]) == findroot(area[s2y][s2x]):
            print(t)
            break
        nxtMelt = []
        for water in melting: # water 주변의 ice가 녹음
            y, x = water[0], water[1] # 현재 물의 가장자리
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i] # 가장자리 주변의 좌표
                if 0 <= ny < R and 0 <= nx < C:
                    if area[ny][nx] == -1: # 주변 얼음을 녹임
                        area[ny][nx] = area[y][x]
                        nxtMelt.append([ny, nx]) # 가장자리에 추가
                        for k in range(4): # 녹은 위치 주변에 다른 idx가 있는지 확인
                            ny2, nx2 = ny + dy[i], nx + dx[i]
                            if 0 <= ny2 < R and 0 <= nx2 < C and area[ny2][nx2] != -1: # 다른 area 만났음
                                if findroot(area[ny][nx]) != findroot(area[ny2][nx2]):
                                    joint(area[ny][nx], area[ny2][nx2])
                    else: # 주변 물과 합치는 과정 수행
                        if findroot(area[y][x]) != findroot(area[ny][nx]):
                            joint(area[y][x], area[ny][nx])
        melting = [nxtMelt[i] for i in range(len(nxtMelt))]
        t += 1


def joint(idx1, idx2): # idx1 과 idx2를 합침
    global rootIdx
    root1, root2 = findroot(idx1), findroot(idx2)
    if root1 != root2: # 서로 다른 그룹일 때
        rootIdx[root2] = rootIdx[root1]


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
