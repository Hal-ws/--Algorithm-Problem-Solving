def main():
    N = int(input())
    command = input()
    board = [[0 for j in range(2 * N + 1)] for i in range(2 * N + 1)]
    board[N][N] = '.'
    y, x = N, N
    dy, dx = [1, 0, -1, 0], [0, -1, 0, 1]
    d = 0
    for c in command:
        if c == 'R':
            d = (d + 1) % 4
        elif c == 'L':
            d -= 1
            if d == -1:
                d = 3
        else:
            y, x = y + dy[d], x + dx[d]
            board[y][x] = '.'
    upBound, downBound, leftBound, rightBound = -1, 0, -1, 0
    for i in range(2 * N + 1):
        for j in range(2 * N + 1):
            if board[i][j] == '.':
                downBound = i
                if upBound == -1:
                    upBound = i
    for j in range(2 * N + 1):
        for i in range(2 * N + 1):
            if board[i][j] == '.':
                rightBound = j
                if leftBound == -1:
                    leftBound = j
    for i in range(upBound, downBound + 1):
        for j in range(leftBound, rightBound + 1):
            if board[i][j] == '.':
                print('.', end='')
            else:
                print('#', end='')
        print()


if __name__ == '__main__':
    main()
