import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    board = [[0 for j in range(m)] for i in range(n)]
    safe = [[1 for j in range(m)] for i in range(n)] # 안전한곳을 1로 표시
    Queens, Knights = [], []
    dy, dx = [-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1] # knight move
    qInfo = list(map(int, sys.stdin.readline().split()))
    kInfo = list(map(int, sys.stdin.readline().split()))
    pInfo = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(qInfo), 2):
        Queens.append([qInfo[i] - 1, qInfo[i + 1] - 1])
    for i in range(1, len(kInfo), 2):
        Knights.append([kInfo[i] - 1, kInfo[i + 1] - 1])
    for i in range(1, len(pInfo), 2):
        y, x = pInfo[i] - 1, pInfo[i + 1] - 1
        safe[y][x] = 0
        board[y][x] = 'P'
    for kP in Knights:
        y, x = kP[0], kP[1]
        board[y][x] = 'K'
        safe[y][x] = 0
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 0:
                safe[ny][nx] = 0
    for qP in Queens:
        y, x = qP[0], qP[1]
        safe[y][x] = 0
        for i in range(y - 1, -1, -1): # 위로 올라감
            if board[i][x] != 0: # 빈칸이 아니면
                break
            safe[i][x] = 0
        for i in range(y + 1, n): #아래로 내려감
            if board[i][x] != 0:
                break
            safe[i][x] = 0
        for j in range(x - 1, -1, -1): #왼쪽으로 움직임
            if board[y][j] != 0:
                break
            safe[y][j] = 0
        for j in range(x + 1, m):
            if board[y][j] != 0:
                break
            safe[y][j] = 0
        d = 1
        while 1:
            ny, nx = y - d, x - d
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] != 0:
                    break
                safe[ny][nx] = 0
                d += 1
            else:
                break
        d = 1
        while 1:
            ny, nx = y + d, x + d
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] != 0:
                    break
                safe[ny][nx] = 0
                d += 1
            else:
                break
        d = 1
        while 1:
            ny, nx = y - d, x + d
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] != 0:
                    break
                safe[ny][nx] = 0
                d += 1
            else:
                break
        d = 1
        while 1:
            ny, nx = y + d, x - d
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] != 0:
                    break
                safe[ny][nx] = 0
                d += 1
            else:
                break
    ans = 0
    for i in range(n):
        for j in range(m):
            if safe[i][j]:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
