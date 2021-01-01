import sys
from itertools import product


def main():
    global N
    N = int(sys.stdin.readline())
    board = []
    ans = 0
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    cases = list(product([0, 1, 2, 3], repeat = 5))
    for case in cases:
        tmp = [[0 for j in range(N)] for i in range(N)]
        for i in range(N):
            for j in range(N):
                tmp[i][j] = board[i][j]
        for i in range(5):
            if case[i] == 0:
                up(tmp)
            if case[i] == 1:
                right(tmp)
            if case[i] == 2:
                down(tmp)
            if case[i] == 3:
                left(tmp)
        for i in range(N):
            for j in range(N):
                if ans <= tmp[i][j]:
                    ans = tmp[i][j]
    print(ans)


def up(tmp):
    global N
    sumChk = [[0 for j in range(N)] for i in range(N)]
    for j in range(N):
        mvIdx = 0
        for i in range(1, N):
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
                            tmp[mvIdx + 1][j] = tmp[i][j]
                            if mvIdx + 1 != i: # 움직일수 있음
                                tmp[i][j] = 0
                        mvIdx += 1
                    else: # 다름
                        tmp[mvIdx + 1][j] = tmp[i][j]
                        if mvIdx + 1 != i: # 움직일수 있음
                            tmp[i][j] = 0
                        mvIdx += 1


def down(tmp):
    global N
    sumChk = [[0 for j in range(N)] for i in range(N)]
    for j in range(N):
        mvIdx = N - 1
        for i in range(N - 2, -1, -1):
            if tmp[i][j] != 0:
                if tmp[mvIdx][j] == 0: #빈칸으로 움직임
                    tmp[mvIdx][j] = tmp[i][j]
                    tmp[i][j] = 0
                else: # 빈칸 아닌데로 움직임
                    if tmp[mvIdx][j] == tmp[i][j]: #같은 숫자 움직임
                        if sumChk[mvIdx][j] == 0: #합쳐야함
                            sumChk[mvIdx][j] = 1
                            tmp[mvIdx][j] = tmp[mvIdx][j] * 2
                            tmp[i][j] = 0
                        else: # 못합침
                            tmp[mvIdx - 1][j] = tmp[i][j]
                            if mvIdx - 1 != i:
                                tmp[i][j] = 0
                        mvIdx -= 1
                    else:
                        tmp[mvIdx - 1][j] = tmp[i][j]
                        if mvIdx - 1 != i:
                            tmp[i][j] = 0
                        mvIdx -= 1


def right(tmp):
    global N
    sumChk = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        mvIdx = N - 1
        for j in range(N - 2, -1, -1):
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
                            tmp[mvIdx - 1][j] = tmp[i][j]
                            if mvIdx - 1 != i: #움직일수 있음
                                tmp[i][j] = 0
                        mvIdx -= 1
                    else:
                        tmp[i][mvIdx - 1] = tmp[i][j]
                        if mvIdx - 1 != j: #움직일수 있음
                            tmp[i][j] = 0
                        mvIdx -= 1



def left(tmp):
    global N
    sumChk = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        mvIdx = 0
        for j in range(1, N):
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
                            tmp[mvIdx + 1][j] = tmp[i][j]
                            if mvIdx + 1 != i: #움직일수 있음
                                tmp[i][j] = 0
                        mvIdx += 1
                    else:
                        tmp[i][mvIdx + 1] = tmp[i][j]
                        if mvIdx + 1 != j: #움직일수 있음
                            tmp[i][j] = 0
                        mvIdx += 1


if __name__ == '__main__':
    main()
