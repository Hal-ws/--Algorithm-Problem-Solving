import sys

N = int(sys.stdin.readline())

def drawstars(N):
    if  N == 1:
        return '*'
    size = pow(2, N) - 1
    newList = [0] * size
    smallStar = drawstars(N - 1)
    if N % 2 == 0:
        newList[0] = '*' * ((size * 2) - 1)
        for i in range(1, size // 2 + 1):
            newList[i] = '*' + ' ' * (2 * (size // 2) - 2 * i) + smallStar[i - 1] + ' ' * (2 * (size // 2) - 2 * i) + '*'
        for i in range(size // 2 + 1, size - 1):
            newList[i] = '*' + ' ' * (2 * size - 2 * (1 + i) - 1)+ '*'
        newList[size - 1] = '*'
        return newList
    else:
        newList[0] = '*'
        for i in range(1, size // 2):
            newList[i] = '*' + ' ' * (2 * i - 1) + '*'
        for i in range(size // 2, size - 1):
            newList[i] = '*' + ' ' * (i - size // 2) * 2 + smallStar[i - size // 2] + ' ' * (i - size // 2) * 2 + '*'
        newList[size - 1] = '*' * ((size * 2) - 1)
        return newList

ans = drawstars(N)
if N % 2 == 0:
    for i in range(len(ans)):
        print(' ' * i + ans[i])
else:
    for i in range(len(ans)):
        print(' ' * (len(ans) - 1 - i) + ans[i])

