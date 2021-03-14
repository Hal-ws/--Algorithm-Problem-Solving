import sys


def main():
    while 1:
        N = int(sys.stdin.readline())
        board = [[0 for j in range(9)] for i in range(9)]
        if N == 0:
            break
        for i in range(N):
            U, LU, V, LV = map(str, sys.stdin.readline().split())
            y1, x1 = ord(LU[0]) - 65, int(LU[1]) - 1
            y2, x2 = ord(LV[0]) - 65, int(LV[1]) - 1
            board[y1][x1], board[y2][x2] = int(U), int(V)
        iniVal = list(map(str, sys.stdin.readline().split()))
        for i in range(9):
            y, x = ord(iniVal[i][0]) - 65, int(iniVal[i][1]) - 1
            board[y][x] = i + 1
        for i in range(9):
            for j in range(9):



if __name__ == '__main__':
    main()
