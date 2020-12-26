from collections import deque
import sys


def main():
    global N, M, board
    N, M = map(int, sys.stdin.readline().split())
    board = []
    q = deque()
    for i in range(N):
        board.append(list(sys.stdin.readline()[:M]))
    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                red = [i, j]
                board[i][j] = '.'
            if board[i][j] == "B":
                blue = [i, j]
                board[i][j] = '.'
    state = [red, blue, 0, -1] #redball, blueball, cnt, 시작방향 (-1은 시작)
    q.append(state)
    ans = -1
    while len(q) > 0:
        r, b, cnt, dir = q[0][0], q[0][1], q[0][2], q[0][3] #ball이 사라지면 none을오 표시
        if r == None and b != None:
            ans = cnt
            break
        if r != None and b != None: #두 공이 다 있을때 다음 횟수 고려
            ry, rx, by, bx = r[0], r[1], b[0], b[1]
            if cnt <= 9: #10번 미만으롱 움직인 상태만 추가한다
                if dir != 2: #상으로 갈 수 있을 때
                    if ry <= by:
                        nr = up(r, b)
                        nb = up(b, nr)
                    else:
                        nb = up(b, r)
                        nr = up(r, nb)
                    q.append([nr, nb, cnt + 1, 0])
                if dir != 3: #오른쪽으로 이동가능
                    if bx <= rx: #rball이 더 오른쪽
                        nr = right(r, b)
                        nb = right(b, nr)
                    else:
                        nb = right(b, r)
                        nr = right(r, nb)
                    q.append([nr, nb, cnt + 1, 1])
                if dir != 0: #아래로 이동
                    if by <= ry: #red 먼저 움직임
                        nr = down(r, b)
                        nb = down(b, nr)
                    else:
                        nb = down(b, r)
                        nr = down(r, nb)
                    q.append([nr, nb, cnt + 1, 2])
                if dir != 1: #왼쪽으로 이동
                    if rx <= bx:
                        nr = left(r, b)
                        nb = left(b, nr)
                    else:
                        nb = left(b, r)
                        nr = left(r, nb)
                    q.append([nr, nb, cnt + 1, 3])
        q.popleft()
    print(ans)


def up(mv, stay):
    global N, M, board
    x = mv[1]
    for y in range(mv[0] - 1, -1, -1):
        if stay != None:
            if (y == stay[0] and x == stay[1]) or board[y][x] == "#":
                ny = y + 1
                nxt = [ny, x]
                break
        else:
            if board[y][x] == "#": #다른 볼과 겹칠 때
                ny = y + 1
                nxt = [ny, x]
                break
        if board[y][x] == 'O': #구멍 만남
            nxt = None
            break
    return nxt


def down(mv, stay):
    global N, M, board
    x = mv[1]
    for y in range(mv[0] + 1, N):
        if stay != None:
            if (y == stay[0] and x == stay[1]) or board[y][x] == "#":
                ny = y - 1
                nxt = [ny, x]
                break
        else:
            if board[y][x] == "#": #다른 볼과 겹칠 때
                ny = y - 1
                nxt = [ny, x]
                break
        if board[y][x] == 'O': #구멍 만남
            nxt = None
            break
    return nxt


def right(mv, stay):
    global N, M, board
    y = mv[0]
    for x in range(mv[1] + 1, M):
        if stay != None:
            if (y == stay[0] and x == stay[1]) or board[y][x] == "#":
                nx = x - 1
                nxt = [y, nx]
                break
        else:
            if board[y][x] == "#": #다른 볼과 겹칠 때 or 벽에 부딪힐때
                nx = x - 1
                nxt = [y, nx]
                break
        if board[y][x] == 'O': #구멍 만남
            nxt = None
            break
    return nxt


def left(mv, stay):
    global N, M, board
    y = mv[0]
    for x in range(mv[1] - 1, -1, -1):
        if stay != None:
            if (y == stay[0] and x == stay[1]) or board[y][x] == "#":
                nx = x + 1
                nxt = [y, nx]
                break
        else:
            if board[y][x] == "#": #다른 볼과 겹칠 때
                nx = x + 1
                nxt = [y, nx]
                break
        if board[y][x] == 'O': #구멍 만남
            nxt = None
            break
    return nxt


if __name__ == '__main__':
    main()
