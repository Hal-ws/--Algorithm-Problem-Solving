def getpoint(i, j, startPoint):
    distance = max(abs(i - startPoint[0]), abs(j - startPoint[1]))
    if (i == startPoint[0] - distance or j == startPoint[1] + distance) and j != startPoint[1] - distance:
        layer = distance * 2 - 1
    else:
        layer = distance * 2
    maxVal = pow(layer + 1, 2)
    if layer % 2 == 1: # layer 1, 3, 5 (우상 layer)
        maxPos = [startPoint[0] + layer // 2 + 1, startPoint[1] + layer // 2]
        val = maxVal - (maxPos[0] - i) - (maxPos[1] - j)
    else:
        maxPos = [startPoint[0] - layer // 2, startPoint[1] - layer // 2]
        val = maxVal - (i - maxPos[0]) - (j - maxPos[1])
    return val


def main():
    N = int(input())
    target = int(input())
    paper = [[0 for i in range(N)] for j in range(N)]
    if N % 2 == 0:
        startPoint = [N // 2, N // 2 - 1]
    else:
        startPoint = [N // 2, N // 2]
    paper[startPoint[0]][startPoint[1]] = 1
    for i in range(N):
        for j in range(N):
            if i != startPoint[0] or j != startPoint[1]:
                paper[i][j] = getpoint(i, j, startPoint)
    for i in range(N):
        for j in range(N):
            print(paper[i][j], end=' ')
            if paper[i][j] == target:
                posy = i
                posx = j
        print()
    print(posy + 1, posx + 1)


if __name__ == "__main__":
    main()
