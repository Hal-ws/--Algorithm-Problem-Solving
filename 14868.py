import sys


def main():
    global board, N, roots, dy, dx
    N, K = map(int, sys.stdin.readline().split())
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    board = [[0 for j in range(N)] for i in range(N)]
    roots = [i for i in range(K + 1)] # 0번은 dummy
    spreadList = [] # 가장자리에 있는 위치들 저장
    for cIdx in range(1, K + 1): # 문명 idx
        x, y = map(int, sys.stdin.readline().split())
        x, y = x - 1, N - y
        board[y][x] = cIdx
        spreadList.append([y, x])
    for pos in spreadList: # 초기에 결합된 문명 확인
        y, x = pos[0], pos[1]
        cIdx = board[y][x]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != 0: # 시작하자마자 다른 문명이랑 붙어있음
                nIdx = board[ny][nx]
                union(cIdx, nIdx)
    std = find(1)
    flag = 1
    for node in range(1, K + 1):
        if find(node) != std:
            flag = 0
            break
    if flag:
        print(0)
        return
    t = 1
    while 1:
        spreadList = spread(spreadList)
        std = find(1)
        flag = 1
        for node in range(1, K + 1):
            if find(node) != std:
                flag = 0
                break
        if flag:
            print(t)
            break
        t += 1


def spread(spreadList):
    global board, N, dy, dx
    nxtSpread = []
    for pos in spreadList: #가장자리에 있는 점들
        y, x = pos[0], pos[1]
        cIdx = board[y][x] # 현재 위치의 문명
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] == 0: #빈 지역으로 확산
                    nxtSpread.append([ny, nx])
                    board[ny][nx] = cIdx
                    # 인접한 문명이 없는지 확인
                    for j in range(4):
                        ny2, nx2 = ny + dy[j], nx + dx[j]
                        if 0 <= ny2 < N and 0 <= nx2 < N and board[ny2][nx2] != 0: # 확산된 곳 옆에 인접한 문명이 있음
                            nIdx = board[ny2][nx2]
                            if find(cIdx) != find(nIdx):
                                union(cIdx, nIdx)
                else: # 인접한 문명이 있음
                    nIdx = board[ny][nx]
                    if find(cIdx) != find(nIdx): # 서로 다른 문명일 시에 합쳐줌
                        union(cIdx, nIdx)
    return nxtSpread


def find(node):
    global roots
    if roots[node] == node:
        return node
    roots[node] = find(roots[node])
    return roots[node]


def union(node1, node2):
    global roots
    root1, root2 = find(node1), find(node2)
    if root1 != root2:
        roots[root2] = root1


if __name__ == '__main__':
    main()
