import sys


def main():
    N = int(sys.stdin.readline())
    board = [[0 for i in range(101)] for j in range(101)]
    for i in range(N):
        x, y, d, g = map(int, sys.stdin.readline().split())
        dragon(x, y, d, g, board)
    cnt = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] == 1 and board[i][j + 1] == 1 and board[i + 1][j] == 1 and board[i + 1][j + 1] == 1:
                cnt += 1
    print(cnt)


def dragon(x, y, d, g, board):
    l = pow(2, g)
    directions = [0] + [0] * l
    directions[1] = d #첫번째 방향은 입력받은 d로 한다
    end = 2
    while end <= l:
        start = end // 2
        i = 0
        while start - i > 0:
            if directions[start - i] == 3:
                directions[start + i + 1] = 0
            else:
                directions[start + i + 1] = directions[start - i] + 1
            i += 1
        end *= 2
    board[y][x] = 1
    for i in range(1, l + 1):
        if directions[i] == 0:
            x += 1
        if directions[i] == 1:
            y -= 1
        if directions[i] == 2:
            x -= 1
        if directions[i] == 3:
            y += 1
        board[y][x] = 1


if __name__ == "__main__":
    main()
