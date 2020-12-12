import sys


def main():
    N = int(sys.stdin.readline())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    tornado = [N // 2, N // 2] #최초 토네이도의 좌표
    distance = 1
    cnt = 0
    endflag = 0
    while 1: #좌상단으로 가면 종료
        for i in range(1, distance + 1): #좌로 이동
            tornado[1] -= 1
            if tornado[1] < 0: #토네이도가 밖으로 나감
                endflag = 1
                break
            cnt += movingdust(board, tornado, 2, N)
        if endflag:
            break
        for i in range(1, distance + 1): #하
            tornado[0] += 1
            cnt += movingdust(board, tornado, 3, N)
        distance += 1
        for i in range(1, distance + 1): #우
            tornado[1] += 1
            cnt += movingdust(board, tornado, 0, N)
        for i in range(1, distance + 1): #상
            tornado[0] -= 1
            cnt += movingdust(board, tornado, 1, N)
        distance += 1
    print(cnt)


def movingdust(board, pos, direction, N): #pos에 있는
    out = 0
    y, x = pos[0], pos[1]
    dust = board[y][x]
    left = dust
    if direction == 0:
        moving = dust * 5 // 100
        if 0 <= x + 2 < N:
            board[y][x + 2] += moving
        else:
            out += moving
        left -= moving
        moving = dust * 10 // 100
        if 0 <= y - 1 < N and 0 <= x + 1 < N :
            board[y - 1][x + 1] += moving
        else:
            out += moving
        left -= moving
        if 0 <= y + 1 < N and 0 <= x + 1 < N :
            board[y + 1][x + 1] += moving
        else:
            out += moving
        left -= moving
        moving = dust * 7 // 100
        if 0 <= y - 1 < N:
            board[y - 1][x] += moving
        else:
            out += moving
        left -= moving
        if 0 <= y + 1 < N:
            board[y + 1][x] += moving
        else:
            out += moving
        left -= moving
        moving = dust * 2 // 100
        if 0 <= y - 2 < N:
            board[y - 2][x] += moving
        else:
            out += moving
        left -= moving
        if 0 <= y + 2 < N:
            board[y + 2][x] += moving
        else:
            out += moving
        left -= moving
        moving = dust * 1 // 100
        if 0 <= y - 1 < N and 0 <= x - 1 < N:
            board[y - 1][x - 1] += moving
        else:
            out += moving
        left -= moving
        if 0 <= y + 1 < N and 0 <= x - 1 < N:
            board[y + 1][x - 1] += moving
        else:
            out += moving
        left -= moving
        if 0 <= x + 1 < N:
            board[y][x + 1] += left
        else:
            out += left
    if direction == 1:
        moving = dust * 5 // 100
        if 0 <= y - 2 < N:
            board[y - 2][x] += moving
        else:
            out += moving
        left -= moving
        moving = dust * 10 // 100
        if 0 <= y - 1 < N and 0 <= x - 1 < N:
            board[y - 1][x - 1] += moving
        else:
            out += moving
        left -= moving
        if 0 <= y - 1 < N and 0 <= x + 1 < N:
            board[y - 1][x + 1] += moving
        else:
            out += moving
        left -= moving
        moving = dust * 7 // 100
        if 0 <= x - 1 < N:
            board[y][x - 1] += moving
        else:
            out += moving
        left -= moving
        if 0 <= x + 1 < N:
            board[y][x + 1] += moving
        else:
            out += moving
        left -= moving
        moving = dust * 2 // 100
        if 0 <= x - 2 < N:
            board[y][x - 2] += moving
        else:
            out += moving
        left -= moving
        if 0 <= x + 2 < N:
            board[y][x + 2] += moving
        else:
            out += moving
        left -= moving
        moving = dust * 1 // 100
        if 0 <= y + 1 < N and 0 <= x - 1 < N:
            board[y + 1][x - 1] += moving
        else:
            out += moving
        left -= moving
        if 0 <= y + 1 < N and 0 <= x + 1 < N :
            board[y + 1][x + 1] += moving
        else:
            out += moving
        left -= moving
        if 0 <= y - 1 < N:
            board[y - 1][x] += left
        else:
            out += left
    if direction == 2:
        moving = dust * 5 // 100
        if 0 <= x - 2 < N:
            board[y][x - 2] += moving
        else:
            out += moving
        left -= moving
        moving = dust * 10 // 100
        if 0 <= y - 1 < N and 0 <= x - 1 < N:
            board[y - 1][x - 1] += moving
        else:
            out += moving
        left -= moving
        if 0 <= y + 1 < N and 0 <= x - 1 < N:
            board[y + 1][x - 1] += moving
        else:
            out += moving
        left -= moving
        moving = dust * 7 // 100
        if 0 <= y - 1 < N:
            board[y - 1][x] += moving
        else:
            out += moving
        left -= moving
        if 0 <= y + 1 < N:
            board[y + 1][x] += moving
        else:
            out += moving
        left -= moving
        moving = dust * 2 // 100
        if 0 <= y - 2 < N:
            board[y - 2][x] += moving
        else:
            out += moving
        left -= moving
        if 0 <= y + 2 < N:
            board[y + 2][x] += moving
        else:
            out += moving
        left -= moving
        moving = dust * 1 // 100
        if 0 <= y - 1 < N and 0 <= x + 1 < N:
            board[y - 1][x + 1] += moving
        else:
            out += moving
        left -= moving
        if 0 <= y + 1 < N and 0 <= x + 1 < N:
            board[y + 1][x + 1] += moving
        else:
            out += moving
        left -= moving
        if 0 <= x - 1 < N:
            board[y][x - 1] += left
        else:
            out += left
    if direction == 3:
        moving = dust * 5 // 100
        if 0 <= y + 2 < N:
            board[y + 2][x] += moving
        else:
            out += moving
        left -= moving
        moving = dust * 10 // 100
        if 0 <= y + 1 < N and 0 <= x - 1 < N:
            board[y + 1][x - 1] += moving
        else:
            out += moving
        left -= moving
        if 0 <= y + 1 < N and 0 <= x + 1 < N:
            board[y + 1][x + 1] += moving
        else:
            out += moving
        left -= moving
        moving = dust * 7 // 100
        if 0 <= x - 1 < N:
            board[y][x - 1] += moving
        else:
            out += moving
        left -= moving
        if 0 <= x + 1 < N:
            board[y][x + 1] += moving
        else:
            out += moving
        left -= moving
        moving = dust * 2 // 100
        if 0 <= x - 2 < N:
            board[y][x - 2] += moving
        else:
            out += moving
        left -= moving
        if 0 <= x + 2 < N:
            board[y][x + 2] += moving
        else:
            out += moving
        left -= moving
        moving = dust * 1 // 100
        if 0 <= y - 1 < N and 0 <= x - 1 < N:
            board[y - 1][x - 1] += moving
        else:
            out += moving
        left -= moving
        if 0 <= y - 1 < N and 0 <= x + 1 < N:
            board[y - 1][x + 1] += moving
        else:
            out += moving
        left -= moving
        if 0 <= y + 1 < N:
            board[y + 1][x] += left
        else:
            out += left
    return out


if __name__ == "__main__":
    main()
