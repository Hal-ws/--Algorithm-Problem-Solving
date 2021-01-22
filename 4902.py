import sys


def main():
    cnt = 1
    while 1:
        nList = list(map(int, sys.stdin.readline().split()))
        layer = nList[0]
        if layer == 0:
            break
        else:
            triangle = [[0 for j in range(layer * 2 - 1)] for i in range(layer)]
            nIdx = 1
            maxVal = -160000001
            for i in range(layer):
                for j in range(layer - i - 1, layer + i):
                    triangle[i][j] = nList[nIdx]
                    nIdx += 1
            for i in range(1, layer + 1):
                if i == 1:
                    tmp = max(nList[1:])
                elif i == layer:
                    tmp = sum(nList[1:])
                else:
                    tmp = getsum(triangle, i, layer)
                if tmp >= maxVal:
                    maxVal = tmp
        print('%s. %s' %(cnt, maxVal))
        cnt += 1


def getsum(tri, size, layer):
    result = -160000001
    for i in range(layer - size + 1):
        for j in range(layer - i - 1, layer + i):
            tmp = 0
            for k in range(i + size):
                for l in range(j - (k - i), j + (k - i) + 1):
                    tmp += tri[k][l]
            if result <= tmp:
                result = tmp
    for i in range(size - 1, layer - size + 1):
        for j in range(layer - i, layer + i - (size * 2 - 1) + 1):
            tmp = 0
            for k in range(i, i + size):
                for l in range(j + (k - i), j + (size * 2 - 1) - (k - i)):
                    tmp += tri[k][l]
            if result <= tmp:
                result = tmp
    return result


if __name__ == '__main__':
    main()
