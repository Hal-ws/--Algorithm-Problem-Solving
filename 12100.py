import sys
from itertools import product
from copy import deepcopy


def main():
    global N
    N = int(sys.stdin.readline())
    board = []
    ans = 0
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    cases = list(product([0, 1, 2, 3], repeat = 5))
    for case in cases:
        tmp = deepcopy(board)
        for i in range(5):
            if case[i] == 0:
                updown(tmp, 0, 1)
            if case[i] == 1:
                leftright(tmp, N - 1, -1)
            if case[i] == 2:
                updown(tmp, N - 1, -1)
            if case[i] == 3:
                leftright(tmp, 0, 1)
        for i in range(N):
            for j in range(N):
                if ans <= tmp[i][j]:
                    ans = tmp[i][j]
    print(ans)


def updown(tmp, stdIdx, factor):
    global N
    sumChk = [[0 for j in range(N)] for i in range(N)]
    if factor == 1:
        start, end = 1, N
    else:
        start, end = N - 2, -1
    for j in range(N):
        mvIdx = stdIdx
        for i in range(start, end, factor):
            if tmp[i][j] != 0: #빈칸 아니면 움직임
                if tmp[mvIdx][j] == 0: #비어있는 칸으로 움직임
                    tmp[mvIdx][j] = tmp[i][j]
                    tmp[i][j] = 0
                else:
                    if tmp[i][j] == tmp[mvIdx][j]: #같음
                        if sumChk[mvIdx][j] == 0: # 합쳐야함
                            sumChk[mvIdx][j] = 1
                            tmp[mvIdx][j] = tmp[mvIdx][j] * 2
                            tmp[i][j] = 0
                        else: # 못합침
                            tmp[mvIdx + factor][j] = tmp[i][j]
                            if mvIdx + factor != i: # 움직일수 있음
                                tmp[i][j] = 0
                        mvIdx += factor
                    else: # 다름
                        tmp[mvIdx + factor][j] = tmp[i][j]
                        if mvIdx + factor != i: # 움직일수 있음
                            tmp[i][j] = 0
                        mvIdx += factor


def leftright(tmp, stdIdx, factor):
    global N
    sumChk = [[0 for j in range(N)] for i in range(N)]
    if factor == -1: # right
        start, end = N - 2, -1
    else:
        start, end = 1, N
    for i in range(N):
        mvIdx = stdIdx
        for j in range(start, end, factor):
            if tmp[i][j] != 0:
                if tmp[i][mvIdx] == 0: #빈칸으로 움직임
                    tmp[i][mvIdx] = tmp[i][j]
                    tmp[i][j] = 0
                else:
                    if tmp[i][mvIdx] == tmp[i][j]:
                        if sumChk[i][mvIdx] == 0: #합쳐야함
                            sumChk[i][mvIdx] = 1
                            tmp[i][mvIdx] = tmp[i][mvIdx] * 2
                            tmp[i][j] = 0
                        else:
                            tmp[mvIdx + factor][j] = tmp[i][j]
                            if mvIdx + factor != i: #움직일수 있음
                                tmp[i][j] = 0
                        mvIdx += factor
                    else:
                        tmp[i][mvIdx + factor] = tmp[i][j]
                        if mvIdx + factor != j: #움직일수 있음
                            tmp[i][j] = 0
                        mvIdx += factor


if __name__ == '__main__':
    main()
