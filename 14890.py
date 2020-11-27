import sys


def main():
    N, L = map(int, sys.stdin.readline().split())
    decline = [[0 for i in range(N)] for j in range(N)] #decline 기록된거 확인
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    for i in range(N):
        cnt += horizonchk(board, decline, i, L, N)
    for j in range(N):
        cnt += verticalchk(board, decline, j, L, N)
    print(cnt)


def horizonchk(board, decline, hIdx, L, N):
    flag = 1 #오른쪽 끝까지 도착가능 flag
    for j in range(N - 1): #처음부터 끝까지 다 같음
        if board[hIdx][j] != board[hIdx][j + 1]:
            flag = 0
            break
    if flag:
        return 1
    flag = 1
    #한 줄이 다 같으면 flag는 1로 유지
    j = 1
    while j < N:
        if board[hIdx][j] == board[hIdx][j - 1]:
            j += 1
        elif board[hIdx][j] == board[hIdx][j - 1] + 1: #왼쪽에 설치해야함
            if decline[hIdx][j - 1] != 2: # 왼쪽칸에 설치가능
                if setdeclineh(board, decline, [hIdx, j - 1], L, N, 'l') == 0: #왼쪽칸부터  좌로 L칸까지 설치가능한지 확인
                    flag = 0
            else:
                flag = 0
            j += 1
        elif board[hIdx][j] == board[hIdx][j - 1] - 1: #지금 칸에 설치해야함
            if decline[hIdx][j] != 2: #지금칸에 설치가능
                if setdeclineh(board, decline, [hIdx, j], L, N, 'c') == 0: #지금칸부터 우로 L칸까지 설치가능한지 확인
                    flag = 0
            else:
                flag = 0
            j += 1
        else:
            flag = 0
            break
    if flag:
        return 1
    else: # 가로로 연결안되면 가로 설치된것 다 삭제
        for j in range(N):
            if decline[hIdx][j] == 2:
                decline[hIdx][j] = 0
        return 0


def verticalchk(board, decline, vIdx, L, N):
    flag = 1
    for i in range(N - 1):
        if board[i][vIdx] != board[i + 1][vIdx]:
            flag = 0
            break
    if flag:
        return 1 # 설치 안해도 다 연결돼있음.
    flag = 1
    i = 1
    while i < N:
        if board[i][vIdx] == board[i - 1][vIdx]:
            i += 1
        elif board[i][vIdx] == board[i - 1][vIdx] + 1: #위쪽에 설치해야함
            if decline[i - 1][vIdx] != 1: #바로 위칸에 설치할 공간있음
                if setdeclinev(board, decline, [i - 1, vIdx], L, N, 'u') == 0: #위칸부터 위로 L칸까지 설치가능한지 확인
                    flag = 0
            else: #위칸에 설치못함:
                flag = 0
            i += 1
        elif board[i][vIdx] == board[i - 1][vIdx] - 1: #현재 위치에 설치해야함
            if decline[i][vIdx] != 1: #현재위치에 설치가능한지 확인
                if setdeclinev(board, decline, [i, vIdx], L, N, 'c') == 0: # 현재칸부터 아래로 L칸까지 설치가능한지 확인
                    flag = 0
            else:
                flag = 0
            i += 1
        else:
            flag = 0
            break
    if flag:
        return 1
    else: #세로로 연결안되면 세로로 경사로 설치한것 다 삭제
        for i in range(N):
            if decline[i][vIdx] == 1:
                decline[i][vIdx] = 0
        return 0


def setdeclinev(board, decline, pos, L, N, d): #d: 위에 설치하는지, 지금 위치에 설치하는지 확인
    y, x= pos[0], pos[1]
    if d == 'u':
        if y - (L - 1) < 0: #위로 가다가 over해버림
            return 0
        for i in range(1, L):
            if board[y][x] != board[y - i][x]:
                return 0
            if decline[y - i][x] == 1:
                return 0
        for i in range(L):
            decline[y - i][x] = 1
        return 1
    if d == 'c':
        if y + (L - 1) >= N:
            return 0
        for i in range(1, L):
            if board[y][x] != board[y + i][x]:
                return 0
            if decline[y + i][x] == 1:
                return 0
        for i in range(L):
            decline[y + i][x] = 1
        return 1


def setdeclineh(board, decline, pos, L, N, d): #d: 왼쪽에 설치하는지, 지금 위치에 설치하는지 확인
    y, x = pos[0], pos[1]
    if d == 'l':
        if x - (L - 1) < 0:
            return 0 # 설치 불가능하면 0 리턴함
        for j in range(1, L):
            if board[y][x] != board[y][x - j]: #경사로를 설치 못함(바닥 안평평)
                return 0
            if decline[y][x - j] == 2: #이미 가로경사로가 설치돼 있음
                return 0 
        #다 통과함. 설치가능
        for j in range(L):
            decline[y][x - j] = 2
        return 1
    if d == 'c':
        if x + (L - 1) >= N:
            return 0
        for j in range(1, L):
            if board[y][x] != board[y][x + j]:
                return 0
            if decline[y][x + j] == 2:
                return 0
        for j in range(L):
            decline[y][x + j] = 2
        return 1


if __name__ == "__main__":
    main()
