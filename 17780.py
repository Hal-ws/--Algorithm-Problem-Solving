import sys


def main():
    global N, board, colorBoard
    N, K = map(int, sys.stdin.readline().split())
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    colorBoard = [] # color가
    board =[[[] for j in range(N)] for i in range(N)] # 말들이 쌓인 board
    horses = [[] for i in range(K)] # 0 ~ K - 1번 말 정보
    for i in range(N):
        colorBoard.append(list(map(int, sys.stdin.readline().split())))
    for hIdx in range(K):
        y, x, d = map(int, sys.stdin.readline().split())
        y, x, d = y - 1, x - 1, d - 1
        board[y][x].append(hIdx)
        horses[hIdx] = [y, x, d]
    t = 1
    endFlag = 0
    while 1:
        if t == 1001:
            answer = -1
            break
        for hIdx in range(K): # 각 horse별로 움직임
            y, x, d = horses[hIdx][0], horses[hIdx][1], horses[hIdx][2]
            if board[y][x][0] == hIdx: # 맨 밑에 있는 horse일때만 움직임
                ny, nx = y + dy[d], x + dx[d] # 다음 위치
                if 0 <= ny < N and 0 <= nx < N and colorBoard[ny][nx] != 2: # 이동가능한 경우
                    for tIdx in board[y][x]: # board[y][x]에 쌓여있는 horse들을 ny, nx로 이동
                        horses[tIdx][0] = ny
                        horses[tIdx][1] = nx
                        board[ny][nx].append(tIdx)
                    board[y][x] = []
                    if colorBoard[ny][nx] == 1: # red인 경우 옮긴 말 과 그 위의 말들을 뒤집어준다
                        rList = []
                        sIdx = board[ny][nx].index(hIdx)
                        for i in range(len(board[ny][nx]) - 1, sIdx - 1, -1):
                            rList.append(board[ny][nx][i])
                        for i in range(sIdx, len(board[ny][nx])):
                            board[ny][nx][i] = rList[i - sIdx]
                    if len(board[ny][nx]) >= 4: #옮기고 나서 4 개 이상 쌓였을 때
                        answer = t
                        endFlag = 1
                        break
                else: # 파란색 또는 범위 밖인 경우
                    # 방향전환
                    if d == 0:
                        horses[hIdx][2] = 1
                    if d == 1:
                        horses[hIdx][2] = 0
                    if d == 2:
                        horses[hIdx][2] = 3
                    if d == 3:
                        horses[hIdx][2] = 2
                    d = horses[hIdx][2] # 전환된 방향 저장
                    ny, nx = y + dy[d], x + dx[d]
                    if 0 <= ny < N and 0 <= nx < N and colorBoard[ny][nx] != 2:
                        for tIdx in board[y][x]:
                            horses[tIdx][0] = ny
                            horses[tIdx][1] = nx
                            board[ny][nx].append(tIdx)
                        board[y][x] = []
                        if colorBoard[ny][nx] == 1:  # red인 경우 옮긴 말 과 그 위의 말들을 뒤집어준다
                            rList = []
                            sIdx = board[ny][nx].index(hIdx)
                            for i in range(len(board[ny][nx]) - 1, sIdx - 1, -1):
                                rList.append(board[ny][nx][i])
                            for i in range(sIdx, len(board[ny][nx])):
                                board[ny][nx][i] = rList[i - sIdx]
                        if len(board[ny][nx]) >= 4: #옮기고 나서 4 개 이상 쌓였을 때
                            answer = t
                            endFlag = 1
                            break
        if endFlag:
            break
        t += 1
    print(answer)


if __name__ == '__main__':
    main()
