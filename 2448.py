import sys
from math import log2

N = int(sys.stdin.readline())

def drawStar(size, top, bottom):
    if size % 2  == 0:
        newList = [0] * size
        basicList = drawStar(size // 2, top, bottom // 2)
        for i in range(size // 2):
            newList[i] = basicList[i]
        bB = 3 * pow(2, int(log2((bottom - 2) // 3 * 2))) - 1
        for i in range(size // 2, size):
            newList[i] = basicList[i - size // 2] + ' ' * (bB - (i - size // 2) * 2) + basicList[i - size // 2]
        return newList
    else:
        smallest = ['*',
                    '* *',
                    '*****']
        return smallest

ans = drawStar(N, 0, N - 1)
for i in range(N):
    ans[i] = ' ' * ((N - 1) - i) + ans[i]  + ' ' * ((N - 1) - i)
for i in range(N):
    print(ans[i])
