import sys
from itertools import product
from collections import deque
from copy import deepcopy


def main():
    M, S = map(int, sys.stdin.readline().split())
    paths = list(product([0, 1, 2, 3], repeat=3))
    fBoard =[[[] for j in range(4)] for i in range(4)]
    eBoard = [[[] for j in range(4)] for i in range(4)]
    sBoard = [[deque() for j in range(4)] for i in range(4)]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dsy = [-1, 0, 1, 0]
    dsx = [0, -1, 0, 1]
    for _ in range(M):
        x, y, d = map(int, sys.stdin.readline().split())
        d -= 1
        x -= 1
        y -= 1
        fBoard[x][y].append(d)
    sX, sY = map(int, sys.stdin.readline().split())
    sY, sX = sX, sY
    sX -= 1
    sY -= 1
    for t in range(S):
        newBoard = [[[] for j in range(4)] for i in range(4)]
        ## 복사마법
        for j in range(4):
            for i in range(4):
                for d in fBoard[i][j]:
                    eBoard[i][j].append(d)
        ## 회전하고 이동
        for i in range(4):
            for j in range(4):
                for d in fBoard[i][j]:
                    flag = 0
                    for k in range(8):
                        ny, nx = i + dy[d], j + dx[d]
                        if 0 <= ny < 4 and 0 <= nx < 4 and len(sBoard[ny][nx]) == 0 and (nx != sX or ny != sY):
                            flag = 1
                            break
                        d -= 1
                        if d == -1:
                            d = 7
                    if flag:
                        newBoard[ny][nx].append(d)
                    else:
                        newBoard[i][j].append(d)
        fBoard = deepcopy(newBoard)
        ## 상어가 이동함
        candidates = []
        for path in paths:
            y, x = sY, sX
            flag = 1
            cnt = 0
            visit = [[0 for j in range(4)] for i in range(4)]
            for d in path:
                y = y + dsy[d]
                x = x + dsx[d]
                if 0 <= y < 4 and 0 <= x < 4:
                    if visit[y][x] == 0:
                        cnt += len(fBoard[y][x])
                    visit[y][x] = 1
                else:
                    flag = 0
                    break
            if flag:
                candidates.append([-cnt, path])
        candidates.sort()
        path = candidates[0][1]
        for d in path:
            sY += dsy[d]
            sX += dsx[d]
            if len(fBoard[sY][sX]) > 0:
                sBoard[sY][sX].append(t)
            fBoard[sY][sX] = []
        ## 냄새 사라짐
        for i in range(4):
            for j in range(4):
                if len(sBoard[i][j]) > 0 and sBoard[i][j][0] == t - 2:
                    sBoard[i][j].popleft()
        ## 복제 시작
        for i in range(4):
            for j in range(4):
                for d in eBoard[i][j]:
                    fBoard[i][j].append(d)
                eBoard[i][j] = []
    ans = 0
    for i in range(4):
        for j in range(4):
            ans += len(fBoard[i][j])
    print(ans)


if __name__ == "__main__":
    main()
