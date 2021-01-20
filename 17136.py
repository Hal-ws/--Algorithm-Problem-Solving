import sys
from itertools import product


def main():
    global board, totalArea, cover, ans, paperChk
    board = []
    paperChk = [[[0, 0, 0, 0, 0] for j in range(10)] for i in range(10)]
    cover = [[0 for j in range(10)] for i in range(10)]
    cases = list(product([0, 1, 2, 3, 4, 5], repeat=5))
    sameareas = []
    totalArea = 0
    ans = 26
    for i in range(10):
        board.append(list(map(int, sys.stdin.readline().split())))
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                for k in range(5):
                    paperChk[i][j][k] = getpaper([i, j], k + 1)
                totalArea += 1
    for case in cases:
        tmpArea = case[0] * 1 + case[1] * 4 + case[2] * 9 + case[3] * 16 + case[4] * 25
        if tmpArea == totalArea:
            cnt = sum(case)
            sameareas.append([cnt] + list(case))
    sameareas.sort()
    for case in sameareas:
        dfs(list(case[1:]), [0, 0], case[0], 4, 1)
        if ans != 26:
            break
    if ans == 26:
        print(-1)
    else:
        print(ans)


def dfs(paper, pos, cnt, kIdx, new): #new 새 종이조각으로 넘어간거(1)
    global board, cover, ans, paperChk
    if ans != 26:
        return
    if cover == board and cnt < ans:
        ans = cnt
    if paper[kIdx] == 0: # 해당 idx의 스티커 다붙임
        if kIdx > 0:
            dfs(paper, pos, cnt, kIdx - 1, 1) # 더 작은거 붙이러감
        else:
            return #끝까지 다 붙임
    if new == 1: # 작은 사이즈 스티커로 변경
        flag1 = 0 #붙일 수 있을지 없을지 확인
        for i in range(10):
            for j in range(10):
                if paperChk[i][j][kIdx]: # 넣을 공간 있을때
                    paper[kIdx] -= 1
                    flag2 = covering([i, j], kIdx + 1, 1) #겹치는지 안겹치는지 확인
                    if flag2:
                        if paper[kIdx] > 0: #지금 스티커를 더 붙일 수 있을 시
                            dfs(paper, [i, j], cnt, kIdx, 0) #지금 사이즈 스티커로 계속
                        else:
                            dfs(paper, [i, j], cnt, kIdx - 1, 1) # 작은 스티커로 넘어감
                        covering([i, j], kIdx + 1, -1)
                        flag1 = 1
                    paper[kIdx] += 1
        if flag1 == 0:
            return
    else: # 기존 스티커 사이즈 유지
        flag1 = 0
        y, x = pos[0], pos[1]
        for i in range(y, 10):
            if i == y:
                for j in range(x + 1, 10):
                    if paperChk[i][j][kIdx]:
                        paper[kIdx] -= 1
                        flag2 = covering([i, j], kIdx + 1, 1)  # 겹치는지 안겹치는지 확인
                        if flag2:
                            if paper[kIdx] > 0:  # 지금 스티커를 더 붙일 수 있을 시
                                dfs(paper, [i, j], cnt, kIdx, 0)  # 지금 사이즈 스티커로 계속
                            else:
                                dfs(paper, [i, j], cnt, kIdx - 1, 1)  # 작은 스티커로 넘어감
                            covering([i, j], kIdx + 1, -1)
                            flag1 = 1
                        paper[kIdx] += 1
            else:
                for j in range(10):
                    if paperChk[i][j][kIdx]:
                        paper[kIdx] -= 1
                        flag2 = covering([i, j], kIdx + 1, 1)  # 겹치는지 안겹치는지 확인
                        if flag2:
                            if paper[kIdx] > 0:  # 지금 스티커를 더 붙일 수 있을 시
                                dfs(paper, [i, j], cnt, kIdx, 0)  # 지금 사이즈 스티커로 계속
                            else:
                                dfs(paper, [i, j], cnt, kIdx - 1, 1)  # 작은 스티커로 넘어감
                            covering([i, j], kIdx + 1, -1)
                            flag1 = 1
                        paper[kIdx] += 1
        if flag1 == 0:
            return


def getpaper(pos, size):
    global board
    y, x = pos[0], pos[1]
    for i in range(size):
        for j in range(size):
            if 10 <= y + i or 10 <= x + j:
                return 0
            if board[y + i][x + j] != 1:
                return 0
    return 1


def covering(pos, size, c):
    global cover
    y, x = pos[0], pos[1]
    flag = 1 #올바르게 됐을때
    for i in range(size):
        for j in range(size):
            cover[y + i][x + j] += c
            if cover[y + i][x + j] == 2:
                flag = 0
    if flag:
        return 1
    else:
        for i in range(size):
            for j in range(size):
                cover[y + i][x + j] -= c
        return 0


if __name__ == '__main__':
    main()
