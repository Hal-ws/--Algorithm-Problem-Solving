import sys
from collections import deque


def main():
    global N, dy, dx
    N, M = map(int, sys.stdin.readline().split())
    board = []
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    answer = 0
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    while 1:
        result1 = findGroup(board)
        if result1 == 0:
            break
        for pos in result1:
            board[pos[0]][pos[1]] = ''
        answer += pow(len(result1), 2)
        gravity(board)
        rotation(board)
        gravity(board)
    print(answer)


def findGroup(board):
    global N
    groupList = []
    for i in range(N):
        for j in range(N):
            if board[i][j] != '' and board[i][j] > 0:
                group = bfs(i, j, board)
                if len(group) >= 2:
                    groupList.append([len(group), group])
    if len(groupList) == 0:
        return 0
    groupList.sort(reverse=True)
    maxSize = groupList[0][0]
    list0 = []
    for i in range(len(groupList)):
        if groupList[i][0] < maxSize:
            break
        else:
            list0.append(sorted(groupList[i][1], reverse=True))
    list1 = cntRainbow(list0, board)
    list2 = getStd(list1, board)
    return list2


def bfs(y, x, board):
    global N, dy, dx
    visit = [[0 for j in range(N)] for i in range(N)]
    group = [[y, x]]
    visit[y][x] = 1
    color = board[y][x]
    q = deque()
    q.append([y, x])
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == 0 and (board[ny][nx] == 0 or board[ny][nx] == color):
                q.append([ny, nx])
                visit[ny][nx] = 1
                group.append([ny, nx])
    return group


def cntRainbow(groupList, board):
    result = []
    maxCnt = 0
    for group in groupList:
        cnt = 0
        for pos in group:
            y, x = pos[0], pos[1]
            if board[y][x] == 0:
                cnt += 1
        if cnt < maxCnt:
            continue
        if cnt > maxCnt:
            result = [] # 리셋
            maxCnt = cnt
        result.append(sorted(group))
    return result


def getStd(groupList, board):
    stdList = []
    for i in range(len(groupList)):
        group = groupList[i]
        for pos in group:
            if board[pos[0]][pos[1]] != 0:
                stdList.append([[pos[0], pos[1]], i])
                break
    stdList.sort(reverse=True)
    return groupList[stdList[0][1]]


def gravity(board):
    global N, dy, dx
    for j in range(N):
        for i in range(N - 1, -1, -1):
            if board[i][j] != '' and board[i][j] >= 0:
                for k in range(i, N - 1):
                    if board[k + 1][j] == '':
                        board[k + 1][j], board[k][j] = board[k][j], board[k + 1][j]
                    else:
                        break


def rotation(board):
    global N, dy, dx
    for k in range(N // 2):
        q = deque()
        lu, ld, ru, rd = [k, k], [N - 1 - k, k], [k, N - 1 - k], [N - 1 - k, N - 1 - k]
        rCnt = ru[1] - lu[1]
        for j in range(lu[1], ru[1] + 1):
            q.append(board[lu[0]][j])
        for i in range(ru[0] + 1, rd[0] + 1):
            q.append(board[i][ru[1]])
        for j in range(rd[1] - 1, ld[1] - 1, -1):
            q.append(board[rd[0]][j])
        for i in range(ld[0] - 1, lu[0], -1):
            q.append(board[i][ld[1]])
        for i in range(rCnt):
            q.append(q.popleft())
        for j in range(lu[1], ru[1] + 1):
            board[lu[0]][j] = q.popleft()
        for i in range(ru[0] + 1, rd[0] + 1):
            board[i][ru[1]] = q.popleft()
        for j in range(rd[1] - 1, ld[1] - 1, -1):
            board[rd[0]][j] = q.popleft()
        for i in range(ld[0] - 1, lu[0], -1):
            board[i][ld[1]] = q.popleft()


if __name__ == '__main__':
    main()
