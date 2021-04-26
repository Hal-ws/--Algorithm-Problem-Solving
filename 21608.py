import sys


def main():
    global dy, dx
    N = int(sys.stdin.readline())
    prefer = [None for i in range(N * N + 1)]
    board = [[0 for j in range(N)] for i in range(N)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    answer = 0
    sList = []
    for i in range(N * N):
        tmpList = list(map(int, sys.stdin.readline().split()))
        sList.append(tmpList[0])
        tmpList = tmpList[1:]
        prefer[sList[i]] = tmpList
    for i in range(N * N):
        sIdx = sList[i]
        list1 = con1(prefer[sIdx], board, N)
        list2 = con2(list1, board, N)
        pos = con3(list2)
        board[pos[0]][pos[1]] = sIdx
    for i in range(N):
        for j in range(N):
            sIdx = board[i][j]
            pList = prefer[sIdx]
            cnt = 0
            for k in range(4):
                ny, nx = i + dy[k], j + dx[k]
                if 0 <= ny < N and 0 <= nx < N and board[ny][nx] in pList:
                    cnt += 1
            if cnt != 0:
                answer += pow(10, cnt - 1)
    print(answer)

        
def con1(pList, board, N):
    global dy, dx
    tmpList = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                cnt = 0
                for k in range(4):
                    ny, nx = i + dy[k], j + dx[k]
                    if 0 <= ny < N and 0 <= nx < N and board[ny][nx] in pList:
                        cnt += 1
                tmpList.append([cnt, i, j])
    tmpList.sort(reverse=True)
    maxCnt = tmpList[0][0]
    result = []
    for i in range(len(tmpList)):
        if tmpList[i][0] == maxCnt:
            result.append([tmpList[i][1], tmpList[i][2]])
        else:
            break
    return result


def con2(list1, board, N):
    global dy, dx
    tmpList = []
    for pos in list1:
        cnt = 0
        y, x = pos[0], pos[1]
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:
                cnt += 1
        tmpList.append([cnt, y, x])
    tmpList.sort(reverse=True)
    maxCnt = tmpList[0][0]
    result = []
    for i in range(len(tmpList)):
        if tmpList[i][0] == maxCnt:
            result.append([tmpList[i][1], tmpList[i][2]])
        else:
            break
    return result


def con3(posList):
    posList.sort()
    return posList[0]


if __name__ == '__main__':
    main()
