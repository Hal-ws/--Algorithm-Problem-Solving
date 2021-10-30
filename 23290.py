import sys
from itertools import product
from collections import deque
from copy import deepcopy


def main():
    M, S = map(int, sys.stdin.readline().split())
    paths = list(product([2, 0, 6, 4], repeat=3))
    fBoard =[[[] for j in range(4)] for i in range(4)]
    eBoard = [[[] for j in range(4)] for i in range(4)]
    sBoard = [[deque() for j in range(4)] for i in range(4)]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
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
        print('%sth try start' %t)
        print('fBoard')
        for i in range(4):
            print(fBoard[i])
        print('sY, sX: %s, %s' %(sY, sX))
        ## 복사마법
        for j in range(4):
            for i in range(4):
                for d in fBoard[i][j]:
                    eBoard[i][j].append(d)
        ## 회전하고 이동
        print('start rotation')
        for i in range(4):
            for j in range(4):
                for d in fBoard[i][j]:
                    print('y, x, d: %s, %s, %s' %(y, x, d))
                    for k in range(8):
                        d -= 1
                        if d == -1:
                            d = 7
                        ny, nx = i + dy[d], j + dx[d]
                        if 0 <= ny < 4 and 0 <= nx < 4 and len(sBoard[ny][nx]) == 0 and (nx != sX or ny != sY):
                            print('ny, nx: %s, %s' %(ny, nx))
                            break
                    newBoard[ny][nx].append(d)
        fBoard = deepcopy(newBoard)
        print('after move')
        for i in range(4):
            print(fBoard[i])
        ## 상어가 이동함
        candidates = []
        for path in paths:
            y, x = sY, sX
            flag = 1
            cnt = 0
            for d in path:
                y = y + dy[d]
                x = x + dx[d]
                if 0 <= y < 4 and 0 <= x < 4:
                    cnt += len(fBoard[y][x])
                else:
                    flag = 0
                    break
            if flag:
                candidates.append([-cnt, path])
        candidates.sort()
        path = candidates[0][1]
        print(candidates)
        for d in path:
            sY += dy[d]
            sX += dx[d]
            fBoard[sY][sX] = []
            sBoard[sY][sX].append(t)
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
    ans = 0
    for i in range(4):
        for j in range(4):
            ans += len(fBoard[i][j])
    print(ans)


if __name__ == "__main__":
    main()
