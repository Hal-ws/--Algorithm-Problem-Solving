import sys
from itertools import product
from copy import deepcopy


def main():
    N = int(sys.stdin.readline())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    cases = list(product([0, 1, 2, 3], repeat=5))
    ans = 0
    for case in cases:
        newBoard = deepcopy(board)
        result = getResult(newBoard, case, N)
        if result > ans:
            ans = result
    print(ans)


def getResult(newBoard, mList, N):
    result = 0
    for d in mList:
        move(newBoard, d, N)
    for i in range(N):
        for j in range(N):
            if newBoard[i][j] > result:
                result = newBoard[i][j]
    return result


def move(newBoard, d, N):  # d: 0, 1, 2, 3 -> 상, 하, 좌, 우
    sumChk = [[0 for j in range(N)] for i in range(N)]
    if d == 0:
        for x in range(N):
            for y in range(N):
                if newBoard[y][x] > 0:
                    for i in range(y - 1, -1, -1):
                        if newBoard[i][x] == 0:
                            newBoard[i][x], newBoard[i + 1][x] = newBoard[i + 1][x], newBoard[i][x]
                        elif newBoard[i][x] == newBoard[i + 1][x] and sumChk[i][x] == 0:
                            sumChk[i][x] = 1
                            newBoard[i][x] *= 2
                            newBoard[i + 1][x] = 0
                            break
                        else:
                            break
    if d == 1:
        for x in range(N):
            for y in range(N - 1, -1, -1):
                if newBoard[y][x] > 0:
                    for i in range(y + 1, N):
                        if newBoard[i][x] == 0:
                            newBoard[i][x], newBoard[i - 1][x] = newBoard[i - 1][x], newBoard[i][x]
                        elif newBoard[i][x] == newBoard[i - 1][x] and sumChk[i][x] == 0:
                            sumChk[i][x] = 1
                            newBoard[i][x] *= 2
                            newBoard[i - 1][x] = 0
                            break
                        else:
                            break
    if d == 2:
        for y in range(N):
            for x in range(N):
                if newBoard[y][x] > 0:
                    for j in range(x - 1, -1, -1):
                        if newBoard[y][j] == 0:
                            newBoard[y][j], newBoard[y][j + 1] = newBoard[y][j + 1], newBoard[y][j]
                        elif newBoard[y][j] == newBoard[y][j + 1] and sumChk[y][j] == 0:
                            sumChk[y][j] = 1
                            newBoard[y][j] *= 2
                            newBoard[y][j + 1] = 0
                            break
                        else:
                            break
    if d == 3:
        for y in range(N):
            for x in range(N - 1, -1, -1):
                if newBoard[y][x] > 0:
                    for j in range(x + 1, N):
                        if newBoard[y][j] == 0:
                            newBoard[y][j], newBoard[y][j - 1] = newBoard[y][j - 1], newBoard[y][j]
                        elif newBoard[y][j] == newBoard[y][j - 1] and sumChk[y][j] == 0:
                            sumChk[y][j] = 1
                            newBoard[y][j] *= 2
                            newBoard[y][j - 1] = 0
                            break
                        else:
                            break


if __name__ == "__main__":
    main()
