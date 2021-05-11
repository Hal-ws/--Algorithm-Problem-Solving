import sys


def main():
    N = int(sys.stdin.readline())
    board = [[0 for j in range(101)] for i in range(101)]
    ans = 0
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        y = 100 - y
        for j in range(x, x + 10):
            for i in range(y, y - 10, -1):
                board[i][j] = 1
    for i in range(92):
        for j in range(92):
            if board[i][j]:
                for x in range(j, 101):
                    if board[i][x]: #1일 경우
                        w = x - j + 1
                    else:
                        break
                minH = 101
                for x in range(j, j + w + 1):
                    for y in range(i, 101):
                        if board[y][x]:
                            h = y - i + 1
                        else:
                            break
                    if h < minH:
                        minH = h
                size1 = minH * w
                for y in range(i, 101):
                    if board[y][j]:
                        h = y - i + 1
                    else:
                        break
                minW = 101
                for y in range(i, i + h + 1):
                    for x in range(j, 101):
                        if board[y][x]:
                            w = x - j + 1
                        else:
                            break
                    if w < minW:
                        minW = w
                size2 = h * minW
                if ans < max(size1, size2):
                    ans = max(size1, size2)
    print(ans)


if __name__ == '__main__':
    main()
