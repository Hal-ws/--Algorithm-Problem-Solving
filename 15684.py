import sys
from itertools import combinations


def main():
    N, M, H = map(int, sys.stdin.readline().split())
    board = [[0 for i in range(2 * N)] for j in range(H + 1)]
    for i in range(M):
        a, b= map(int, sys.stdin.readline().split())
        x = b * 2 - 1 #line 의 x축 index 표현
        board[a][x + 1] = 1
    for i in range(H + 1):
        for j in range(2 * N):
            if j % 2 == 1:
                board[i][j] = '*'
    posList = [] # 사다리를 놓을 수 있는 위치를 저장
    for i in range(1, H + 1):
        for j in range(2, 2 * N - 1, 2):
            flag = 1
            if board[i][j] == 1:
                flag = 0
            if j < 2 * N - 2:
                if board[i][j + 2] == 1:
                    flag = 0
            if board[i][j - 2] == 1:
                flag = 0
            if flag:
                posList.append([i, j])
    # 0개, 1개, 2개, 3개를 이용할 때 답이 되는게 있는지 확인해본다
    ansflag = 1 # 답을 찾았음
    for x in range(1, 2 * N, 2):
        arrivex= arriveChk(board, x, N, H)
        if x != arrivex:
            ansflag = 0 #이 case는 답이 안되는걸로 판정
            break
    if ansflag: #위에서 답이 나옴
        print(0)
        return 0
    else: #위에서 답 못찾음
        case = list(combinations(posList, 1))
        lc = len(case)
        for i in range(lc):
            ansflag = 1
            for j in range(len(case[i])): #case[i]에 있는 포지션대로 사다리 설치
                board[case[i][j][0]][case[i][j][1]] = 1
            for x in range(1, 2 * N, 2):
                arrivex = arriveChk(board, x, N, H)
                if x != arrivex:
                    ansflag = 0  # case[i]의 경우에는 답이 안됨
                    break
            if ansflag:
                break
            else:
                for j in range(len(case[i])):  #case[i]의 경우에 답이 안나왔기 때문에 원복
                    board[case[i][j][0]][case[i][j][1]] = 0
    if ansflag: #위에서 답이 나옴
        print(1)
        return 0
    else:
        case = list(combinations(posList, 2))
        lc = len(case)
        for i in range(lc):
            ansflag = 1
            for j in range(len(case[i])):  # case[i]에 있는 포지션대로 사다리 설치
                board[case[i][j][0]][case[i][j][1]] = 1
            for x in range(1, 2 * N, 2):
                arrivex = arriveChk(board, x, N, H)
                if x != arrivex:
                    ansflag = 0  # case[i]의 경우에는 답이 안됨
                    break
            if ansflag:
                break
            else:
                for j in range(len(case[i])):  # case[i]의 경우에 답이 안나왔기 때문에 원복
                    board[case[i][j][0]][case[i][j][1]] = 0
    if ansflag:
        print(2)
        return 0
    else:
        case = list(combinations(posList, 3))
        lc = len(case)
        for i in range(lc):
            ansflag = 1
            for j in range(len(case[i])):  # case[i]에 있는 포지션대로 사다리 설치
                board[case[i][j][0]][case[i][j][1]] = 1
            for x in range(1, 2 * N, 2):
                arrivex = arriveChk(board, x, N, H)
                if x != arrivex:
                    ansflag = 0  # case[i]의 경우에는 답이 안됨
                    break
            if ansflag:
                break
            else:
                for j in range(len(case[i])):  # case[i]의 경우에 답이 안나왔기 때문에 원복
                    board[case[i][j][0]][case[i][j][1]] = 0
    if ansflag:
        print(3)
        return 0
    else:
        print(-1)


def arriveChk(board, x, N, H): # [1, x]에서 시작해서 도착하는 지점이 어디인지 확인
    y = 1
    while y < H + 1:
        if board[y][x - 1] == 1:
            x -= 2
        elif x != 2 * N - 1: # 맨 오른쪽 끝에 있는 줄이 아닐때
            if board[y][x + 1] == 1:
                x += 2
        y += 1
    return x # 도착한 지점의 x

if __name__ == "__main__":
    main()
