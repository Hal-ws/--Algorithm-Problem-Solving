import sys
from itertools import product


def main():
    global board, totalArea
    board = []
    totalArea = 0
    for i in range(10):
        board.append(list(map(int, sys.stdin.readline().split())))
    paperChk = [[[0, 0, 0, 0, 0] for j in range(10)] for i in range(10)]
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                for k in range(5):
                    paperChk[i][j][k] = getpaper([i, j], k + 1)
                totalArea += 1
    cases = list(product([0, 1, 2, 3, 4, 5, 6], repeat=5))
    for case in cases:
        tmpArea = case[0] * 1 + case[1] * 4 + case[2] * 9 + case[3] * 16 + case[4] * 25
        if tmpArea == totalArea:
            dfs(case, 0)


def dfs(paper, cnt): #종이를 몇개 썼는지 카운팅
    print(paper)



def getpaper(pos, size):
    global board
    y, x = pos[0], pos[1]
    flag = 1
    for i in range(size):
        for j in range(size):
            if 10 <= y + i or 10 <= x + j:
                flag = 0
                break
            if board[y + i][x + j] != 1:
                flag = 0
                break
    return flag


if __name__ == '__main__':
    main()
