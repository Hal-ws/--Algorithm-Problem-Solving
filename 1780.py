import sys

def checkonepiece(piece):
    l = len(piece)
    std = piece[0][0]
    for i in range(l):
        for j in range(l):
            if piece[i][j] != std:
                return None
    if std == -1:
        return [1, 0, 0]
    elif std == 0:
        return [0, 1, 0]
    else:
        return [0, 0, 1]

def devide(paper, size):
    chk = checkonepiece(paper)
    if chk != None:
        return chk
    upLeft = [0] * (size // 3)
    up = [0] * (size // 3)
    upRight = [0] * (size // 3)
    for i in range(size // 3):
        upLeft[i] = paper[i][:size // 3]
        up[i] = paper[i][size // 3:size * 2 // 3]
        upRight[i] =paper[i][size * 2 // 3:]
    midLeft = [0] * (size // 3)
    mid = [0] * (size // 3)
    midRight = [0] * (size // 3)
    for i in range(size // 3, size * 2 // 3):
        midLeft[i - size // 3] = paper[i][:size // 3]
        mid[i - size // 3] = paper[i][size // 3:size * 2 // 3]
        midRight[i - size // 3] = paper[i][size * 2 // 3:]
    downLeft = [0] * (size // 3)
    downRight = [0] * (size // 3)
    down = [0] * (size // 3)
    for i in range(size * 2 // 3, size):
        downLeft[i - size * 2 // 3] = paper[i][:size // 3]
        down[i - size * 2 // 3] = paper[i][size // 3:size * 2 // 3]
        downRight[i - size * 2 // 3] = paper[i][size * 2 // 3:]
    a = devide(upLeft, size // 3)
    b = devide(up, size // 3)
    c = devide(upRight, size // 3)
    d = devide(midLeft, size // 3)
    e = devide(mid, size // 3)
    f = devide(midRight, size // 3)
    g = devide(downLeft, size // 3)
    h = devide(down, size // 3)
    i = devide(downRight, size // 3)

    return [a[0] + b[0] + c[0] + d[0] + e[0] + f[0] + g[0] + h[0] + i[0], a[1] + b[1] + c[1] + d[1] + e[1] + f[1] + g[1] + h[1] + i[1], a[2] + b[2] + c[2] + d[2] + e[2] + f[2] + g[2] + h[2] + i[2]]

N = int(sys.stdin.readline())
paper = [0] * N
for i in range(N):
    paper[i] = list(map(int, sys.stdin.readline().split()))

ans = devide(paper, N)
print(ans[0])
print(ans[1])
print(ans[2])
