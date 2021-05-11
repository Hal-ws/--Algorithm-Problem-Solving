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
                minW = 101
                for y in range(i, 101):
                    curL = 0
                    for x in range(j, 101):
                        if board[y][x]:
                            curL += 1
                        else:
                            break
                    if curL == 0:
                        break
                    if curL <= minW:
                        minW = curL
                    size = (y - i + 1) * minW
                    if ans < size:
                        ans = size
    print(ans)


if __name__ == '__main__':
    main()
