import sys
from itertools import product, permutations
from _collections import deque


def main():
    global dy, dx, dz
    dz = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dx = [0, 0, 0, 0, -1, 1]
    answer = 3126
    layers = [[] for i in range(5)] # 0 ~ 4번 layer들을 저장. 회전하는걸로 계산한다
    for i in range(5):
        tmp = []
        for j in range(5):
            tmp.append(list(map(int, sys.stdin.readline().split())))
        layers[i].append(tmp)
    for i in range(5):
        for j in range(1, 5): # 1번, 2번
            layers[i].append(rotation(layers[i][0], j)) # i번째 layer의 0번 케이스(회전 안함)를 j번 회전시키고 저장한다
    suffles = list(permutations([0, 1, 2, 3, 4], 5))
    cases = list(product([0, 1, 2, 3], repeat=5))
    for suffle in suffles:
        for case in cases:
            testBox = []
            for i in range(5): # test용 박스 조립
                testBox.append(layers[suffle[i]][case[i]])
            if testBox[4][0][0] == testBox[0][4][4] == 1:
                result = bfs(testBox)
                if result < answer:
                    answer = result
            if answer == 12:
                print(12)
                return
    if answer == 3126:
        print(-1)
    else:
        print(answer)


def bfs(box):
    global dy, dx, dz
    visit = [[[0 for j in range(5)] for i in range(5)] for k in range(5)]
    q = deque()
    if box[4][0][0] == 1: # 가능
        q.append([4, 0, 0, 0]) # z, y, x, cnt
        visit[4][0][0] = 1
    while len(q) > 0:
        tmp = q.popleft()
        z, y, x, cnt = tmp[0], tmp[1], tmp[2], tmp[3]
        if z == 0 and y == 4 and x == 4:
            return cnt
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < 5 and 0 <= ny < 5 and 0 <= nx < 5 and visit[nz][ny][nx] == 0 and box[nz][ny][nx] == 1:
                visit[nz][ny][nx] = 1
                q.append([nz, ny, nx, cnt + 1])
    return 3126


def rotation(layer, rCnt):
    base = [[0 for j in range(5)] for i in range(5)]
    for i in range(5):
        for j in range(5):
            base[i][j] = layer[i][j]
    newLayer = [[0 for j in range(5)] for i in range(5)]
    for _ in range(rCnt):
        for i in range(5):
            for j in range(5):
                newLayer[j][5 - i - 1] = base[i][j]
        for i in range(5):
            for j in range(5):
                base[i][j] = newLayer[i][j]
    return newLayer


if __name__ == '__main__':
    main()
