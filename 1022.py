def main():
    r1, c1, r2, c2 = map(int, input().split())
    plate = [[0 for i in range(c2 - c1 + 1)] for j in range(r2 - r1 + 1)]
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            plate[i - r1][j - c1] = getnum(i, j)
    maxVal = 0
    for i in range(r2 - r1 + 1):
        if max(plate[i]) >= maxVal:
            maxVal = max(plate[i])
    maxLen = len(str(maxVal))
    for i in range(r2 - r1 + 1):
        for j in range(c2 - c1 + 1):
            blank = ' ' * (maxLen - len(str(plate[i][j])))
            print('%s%s' %(blank, plate[i][j]), end=' ')
        print()


def getnum(i, j):
    layer = max(abs(i), abs(j))
    maxVal = pow(2 * layer + 1, 2)
    distance = 0
    if i == layer and j == layer:
        distance = 0
    elif i == (-1) * layer and j == (-1) * layer:
        distance = layer * 4
    elif i == layer or j == (-1) * layer: # 가까운지역
        distance += layer - i
        distance += layer - j
    else:
        distance += layer * 4
        distance += layer + i
        distance += layer + j
    return maxVal - distance


if __name__ == "__main__":
    main()
