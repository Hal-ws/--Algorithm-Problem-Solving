import sys


def main():
    global N, board, bombCnt
    N, M = map(int, sys.stdin.readline().split())
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    bombCnt = [0, 0, 0, 0] # 0번 idx는 dummy
    board = []
    answer = 0
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    cY, cX = N // 2, N // 2 # 중심의 좌표
    for i in range(M):
        d, s = map(int, sys.stdin.readline().split())
        for k in range(1, s + 1):
            y, x = cY + k * dy[d - 1], cX + k * dx[d - 1]
            board[y][x] = 0
        result = tracking(0, [])
        tracking(1, result)
        bomb()
        transform()
    for i in range(1, 4):
        answer += i * bombCnt[i]
    print(answer)


def tracking(flag, numList): # board 에 넣을때는 1, board를 돌면서 list를 얻을때는 0
    global N, board
    maxDis = 1
    l = len(numList)
    if flag:
        idx = 0 #numList에 있는 값들을 board에 삽입
    else:
        result = []
    y, x = N // 2, N // 2
    endflag = 0
    while 1:
        for i in range(maxDis):
            x -= 1
            if flag:
                if idx < l:
                    board[y][x] = numList[idx]
                    idx += 1
                else:
                    board[y][x] = 0
            else:
                if board[y][x] != 0:
                    result.append(board[y][x])
            if y == 0 and x == 0: # 다 순회함
                endflag = 1
                break
        if endflag:
            break
        for i in range(maxDis):
            y += 1
            if flag:
                if idx < l:
                    board[y][x] = numList[idx]
                    idx += 1
                else:
                    board[y][x] = 0
            else:
                if board[y][x] != 0:
                    result.append(board[y][x])
        maxDis += 1
        for i in range(maxDis):
            x += 1
            if flag:
                if idx < l:
                    board[y][x] = numList[idx]
                    idx += 1
                else:
                    board[y][x] = 0
            else:
                if board[y][x] != 0:
                    result.append(board[y][x])
        for i in range(maxDis):
            y -= 1
            if flag:
                if idx < l:
                    board[y][x] = numList[idx]
                    idx += 1
                else:
                    board[y][x] = 0
            else:
                if board[y][x] != 0:
                    result.append(board[y][x])
        maxDis += 1
    if flag == 0:
        return result


def bomb():
    global N, board, bombCnt
    bombList = tracking(0, [])
    bStack = [] # stack에 넣어놓고 폭발
    for i in range(len(bombList)):
        tmp = bombList[i]
        if len(bStack) > 0: # 1개 이상 쌓였을때
            if bStack[-1] == tmp:
                bStack.append(tmp)
            else: # 다름. 앞에서 터뜨릴수 있는게 있는지 다 확인해본다
                if len(bStack) >= 4 and bStack[-1] == bStack[-2] == bStack[-3] == bStack[-4]:
                    std = bStack[-1]
                    cnt = 0
                    while 1:
                        if bStack[-1] == std:
                            cnt += 1
                            bStack.pop()
                        else:
                            break
                        if len(bStack) == 0:
                            break
                    bombCnt[std] += cnt
                bStack.append(tmp)
        else:
            bStack.append(tmp)
    if len(bStack) >= 4 and bStack[-1] == bStack[-2] == bStack[-3] == bStack[-4]:
        std = bStack[-1]
        cnt = 0
        while 1:
            if bStack[-1] == std:
                cnt += 1
                bStack.pop()
            else:
                break
            if len(bStack) == 0:
                break
        bombCnt[std] += cnt
    tracking(1, bStack)


def transform():
    global N, board, bombCnt
    numList = tracking(0, [])
    numList.append(10)
    tList = []
    cnt, num = 1, numList[0]
    for i in range(1, len(numList)):
        tmp = numList[i]
        if tmp == num:
            num = tmp
            cnt += 1
        else: # 다르다.
            tList.append(cnt)
            tList.append(num)
            cnt = 1
            num = numList[i]
    tracking(1, tList)
    return 0


if __name__ == '__main__':
    main()
