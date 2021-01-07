import sys
from itertools import product


def main():
    global board, cover, paper, ans, area, totalArea
    board, cover = [], []
    ans, area, totalArea = 26, 0, 0
    for i in range(10):
        board.append(list(map(int, sys.stdin.readline().split())))
        cover.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                totalArea += 1
    cases = list(product([0, 1, 2, 3, 4, 5], repeat=5))
    possible = []
    for paper in cases:
        cnt = sum(paper) #사용한 조각 수
        if paper[0] * 1 + paper[1] * 4 + paper[2] * 9 + paper[3] * 16 + paper[4] * 25 == totalArea:
            possible.append([cnt, list(paper)])
    possible.sort()
    for case in possible:
        dfs(case[1], [0, 0], case[0], 4)
        if ans != 26:
            break
    if ans == 26:
        print(-1)
    else:
        print(ans)


def dfs(paper, pos, cnt, sizeIdx):
    global board, cover, ans
    y, x = pos[0], pos[1]
    print('paper: %s' %paper)
    for i in range(10):
        print(cover[i])
    print('-------------------')
    if ans != 26:
        return
    if cover == board:
        ans = cnt
    for i in range(y, 10 - sizeIdx):
        if i == y:
            for j in range(x, 10 - sizeIdx):
                if board[i][j] == 1 and cover[i][j] == 0:
                    possible = chkSize([i, j], sizeIdx + 1)  #sizeIdx 개만큼 공간 있는지 확인
                    if possible[sizeIdx] and paper[sizeIdx] > 0:  # 붙일 공간이 있고, 붙일 종이조각이 남아있음
                        paper[sizeIdx] -= 1
                        covering([i, j], sizeIdx + 1, 1)
                        dfs(paper, [i, j], cnt)
                        paper[sizeIdx] += 1
                        covering([i, j], sizeIdx + 1, 0)


def covering(pos, size, c):
    global cover
    y, x = pos[0], pos[1]
    cnt = 0
    for i in range(size):
        for j in range(size):
            cover[y + i][x + j] = c
            cnt += 1


def chkSize(pos, size): #pos를 맨 왼쪽위로 한 종이조각의 크기
    global board, cover
    y, x = pos[0], pos[1]
    flag = 1
    for i in range(y, y + size):
        for j in range(x, x + size):
            if board[i][j] == 1:
                flag = 0
                break
            if cover[i][j] == 1:
                flag = 0
                break
    return flag


if __name__ == '__main__':
    main()
