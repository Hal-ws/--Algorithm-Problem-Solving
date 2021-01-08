import sys
from itertools import product


def main():
    global board, cover, paper, areaChk, ans, area, totalArea
    cases = list(product([0, 1, 2, 3, 4, 5], repeat=5))
    board, cover, possible = [], [], []
    ans, area, totalArea = 26, 0, 0
    areaChk = [[[0, 0, 0, 0, 0] for j in range(10)] for i in range(10)]
    for i in range(10): #board, cover 더하고 총 넓이 구함
        board.append(list(map(int, sys.stdin.readline().split())))
        cover.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        for j in range(10):
            if board[i][j] == 1:
                totalArea += 1
    for i in range(10): #areaChk 완성
        for j in range(10):
            getarea([i, j])
    for paper in cases:
        cnt = sum(paper) #사용한 조각 수
        if paper[0] * 1 + paper[1] * 4 + paper[2] * 9 + paper[3] * 16 + paper[4] * 25 == totalArea:
            possible.append([cnt, list(paper)])
    possible.sort()
    for case in possible:
        print('case[1]: %s' %case[1])
        dfs(case[1], [0, 0], case[0], 0, 4)
        if ans != 26:
            break
    if ans == 26:
        print(-1)
    else:
        print(ans)


def dfs(case, pos, cnt, same, kIdx):
    global board, cover, ans, areaChk
    y, x = pos[0], pos[1]
    if ans != 26:
        return
    if cover == board:
        ans = cnt
        return
    print('kIdx, pos: %s, %s' %(kIdx, pos))
    if case[kIdx] == 0:
        if kIdx == 0:
            covering([0, 0], 10, 0)
            return
        dfs(case, pos, cnt, 0, kIdx - 1)
    else: #아직 kIdx째 색종이를 붙일게 남아있음
        if same: #이전에 붙였던 색종이랑 같은 색종이를 붙일때
            flag = 0
            for i in range(y, 10 - kIdx):
                for j in range(x, 10 - kIdx):
                    if areaChk[i][j][kIdx]: #가능할때
                        flag2 = 1
                        for k in range(i, i + kIdx + 1):
                            for l in range(j, j + kIdx + 1):
                                if cover[k][l] == 1:
                                    flag2 = 0
                                    break
                        if flag2:
                            print('i, j: %s, %s' %(i, j))
                            print('case: %s' %case)
                            flag = 1 #가능한 곳을 찾았을때
                            covering([i, j], kIdx + 1, 1)
                            for i in range(10):
                                print(cover[i])
                            if paper[kIdx] >= 1:
                                case[kIdx] -= 1
                                dfs(case, [i, j], cnt, 1, kIdx)
                                case[kIdx] += 1
                            else:
                                dfs(case, [i, j], cnt, 0, kIdx - 1)
            if flag == 0:
                covering([0, 0], 10, 0)
                return # 못붙임. return
        else: #다른 색종이를 붙일때
            flag = 0
            for i in range(10 - kIdx): #[0, 0]부터 끝까지 확인해본다
                for j in range(10 - kIdx):
                    if areaChk[i][j][kIdx]:  # 가능할때
                        flag2 = 1
                        for k in range(i, i + kIdx + 1):
                            for l in range(j, j + kIdx + 1):
                                if cover[k][l] == 1:
                                    flag2 = 0
                                    break
                        if flag2:
                            flag = 1  # 가능한 곳을 찾았을때
                            covering([i, j], kIdx + 1, 1)
                            if paper[kIdx] >= 1:
                                dfs(case, [i, j], cnt, 1, kIdx)
                            else:
                                dfs(case, [i, j], cnt, 0, kIdx - 1)
            if flag == 0:
                covering([0, 0], 10, 0)
                return  # 못붙임. return


def getarea(pos):
    global areaChk, board
    y, x = pos[0], pos[1]
    for k in range(1, 6):
        flag = 1
        for i in range(y, y + k):
            for j in range(x, x + k):
                if 10 <= i or 10 <= j:
                    flag = 0
                    break
                if board[i][j] == 0:
                    flag = 0
                    break
        if flag:
            areaChk[y][x][k - 1] = 1


def covering(pos, size, c):
    global cover
    y, x = pos[0], pos[1]
    cnt = 0
    for i in range(size):
        for j in range(size):
            cover[y + i][x + j] = c
            cnt += 1


if __name__ == '__main__':
    main()
