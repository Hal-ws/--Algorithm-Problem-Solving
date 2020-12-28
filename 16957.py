import sys


def main():
    global R, C, board, arrive
    R, C = map(int, sys.stdin.readline().split())
    board = []
    for i in range(R):
        board.append(list(map(int, sys.stdin.readline().split())))
    arrive = [[0 for j in range(C)] for i in range(R)] #최종 도착장소
    for i in range(R):
        for j in range(C):
            if arrive[i][j] == 0:
                getsol([i, j])
    ans = [[0 for j in range(C)] for i in range(R)]
    for i in range(R):
        for j in range(C):
            targetY, targetX = arrive[i][j][0], arrive[i][j][1]
            ans[targetY][targetX] += 1
    for i in range(R):
        for j in range(C):
            print(ans[i][j], end=' ')
        print()


def getsol(pos):
    global R, C, board, arrive
    dy, dx = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
    q = [pos]
    endflag = 0
    arriveP = 0 #도착 지점 저장
    while 1:
        y, x = q[-1][0], q[-1][1]
        minVal = 300001
        nxt = []
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                tmp = board[ny][nx]
                if tmp <= minVal and tmp <= board[y][x]:
                    minVal = tmp
                    nxt = [ny, nx]
        if minVal == 300001: #도착지 발견. 더이상 갈곳 없음
            arrive[y][x] = [y, x]
            arriveP = [y, x]
            endflag = 1
        else: #구슬이 nxt로 움직임
            if arrive[nxt[0]][nxt[1]] == 0: #다음으로 갈곳도 도착지 안정해져있음
                q.append([nxt[0], nxt[1]])
            else:
                arriveP = arrive[nxt[0]][nxt[1]]
                endflag = 1
        if endflag:
            break
    if arriveP != 0:
        for p in q:
            y, x = p[0], p[1]
            arrive[y][x] = arriveP


if __name__ == '__main__':
    main()
