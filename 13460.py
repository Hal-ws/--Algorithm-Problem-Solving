import sys
from collections import deque


def main():
    N, M = map(int, sys.stdin.readline().split())
    visit = [[[[0 for j in range(M)] for i in range(N)] for k in range(M)] for l in range(N)]
    board = []
    for i in range(N):
        board.append(list(sys.stdin.readline()[:M]))
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'B':
                bPos = [i, j]
                board[i][j] = '.'
            if board[i][j] == 'R':
                rPos = [i, j]
                board[i][j] = '.'
    visit[rPos[0]][rPos[1]][bPos[0]][bPos[1]] = 1
    q = deque()
    q.append([rPos, bPos, 0])  # 붉은공, 파란공, 움직인 횟수
    while len(q) > 0:
        tmp = q.popleft()
        rPos, bPos, cnt = tmp[0], tmp[1], tmp[2]
        if cnt == 10:
            break
        for i in range(4):
            result = move(rPos, bPos, board, i)
            rY, rX, bY, bX = result[1][0], result[1][1], result[2][0], result[2][1]
            if result[0] == 0 and visit[rY][rX][bY][bX] == 0: # 이동 성공. 빨간공만 hole에 집어넣는건 실패
                q.append([[rY, rX], [bY, bX], cnt + 1])
                visit[rY][rX][bY][bX] = 1
            if result[0] == 1: # 빨간공만 hole에 집어넣는것 성공함
                print(cnt + 1)
                return
    print(-1)


def move(rPos, bPos, board, d):
    rY, rX = rPos[0], rPos[1]
    bY, bX = bPos[0], bPos[1]
    board[rY][rX] = 'R'
    board[bY][bX] = 'B'
    dy = [-1, 1, 0, 0]  # d는 상 하 좌 우 순서대로
    dx = [0, 0, -1, 1]
    rFlag, bFlag = 1, 1
    rFirst = 0  # 빨간색이 꼭 먼저 움직여야 하는 상황.
    result = 0
    while 1:
        if rFlag + bFlag == 0:
            break
        if d == 0:
            if rY < bY:
                rFirst = 1
        if d == 1:
            if rY > bY:
                rFirst = 1
        if d == 2:
            if rX < bX:
                rFirst = 1
        if d == 3:
            if rX > bX:
                rFirst = 1
        if rFirst:  # 빨간색 먼저 움직인다
            if rFlag:
                nxtRY, nxtRX = rY + dy[d], rX+ dx[d]
                if board[nxtRY][nxtRX] == 'O':
                    rFlag = 0  # 붉은 공은 더이상 못움직임
                    board[rY][rX] = '.'
                    result = 1
                elif board[nxtRY][nxtRX] == '.':
                    board[nxtRY][nxtRX] = 'R'
                    board[rY][rX] = '.'
                    rY, rX = nxtRY, nxtRX
                else:
                    rFlag = 0
            if bFlag:
                nxtBY, nxtBX = bY + dy[d], bX + dx[d]
                if board[nxtBY][nxtBX] == 'O':
                    board[bY][bX] = '.'
                    result = -1
                    break
                elif board[nxtBY][nxtBX] == '.':
                    board[nxtBY][nxtBX] = 'R'
                    board[bY][bX] = '.'
                    bY, bX = nxtBY, nxtBX
                else:
                    bFlag = 0
        else: # 파란색 먼저 움직인다
            if bFlag:
                nxtBY, nxtBX = bY + dy[d], bX + dx[d]
                if board[nxtBY][nxtBX] == 'O':
                    board[bY][bX] = '.'
                    result = -1
                    break
                elif board[nxtBY][nxtBX] == '.':
                    board[nxtBY][nxtBX] = 'B'
                    board[bY][bX] = '.'
                    bY, bX = nxtBY, nxtBX
                else:
                    bFlag = 0
            if rFlag:
                nxtRY, nxtRX = rY + dy[d], rX + dx[d]
                if board[nxtRY][nxtRX] == 'O':
                    rFlag = 0  # 붉은 공은 더이상 못움직임
                    board[rY][rX] = '.'
                    result = 1
                elif board[nxtRY][nxtRX] == '.':
                    board[nxtRY][nxtRX] = 'R'
                    board[rY][rX] = '.'
                    rY, rX = nxtRY, nxtRX
                else:
                    rFlag = 0
    board[rY][rX] = '.'
    board[bY][bX] = '.'
    return [result, [rY, rX], [bY, bX]]


if __name__ == "__main__":
    main()
