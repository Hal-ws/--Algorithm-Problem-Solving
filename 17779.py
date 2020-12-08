import sys


def main():
    N = int(sys.stdin.readline())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    minDiff = [99999999999999]
    for i in range(N - 2):
        for j in range(1, N - 1):
            dfs(board, [i, j], None, None, minDiff, N)
    print(minDiff[0])


def dfs(board, up, left, down, minDiff, N):
    if left == None:
        leftY, leftX =up[0] + 1, up[1] - 1
        while 1:
            if leftY < N - 1 and leftX >= 0:
                dfs(board, up, [leftY, leftX], None, minDiff, N)
                leftY += 1
                leftX -= 1
            else:
                break
    elif down == None:
        downY, downX = left[0] + 1, left[1] + 1
        while 1:
            if downX < N - 1 and downY < N:
                dfs(board, up, left, [downY, downX], minDiff, N)
                downY += 1
                downX += 1
            else:
                break
    else:
        rightX = (up[1] + down[0] + down[1] - up[0]) // 2
        rightY = rightX + up[0] - up[1]
        tmp = getdiff(board, up, left, down, [rightY, rightX], N)
        if tmp <= minDiff[0]:
            minDiff[0] = tmp


def getdiff(board, up, left, down, right, N):
    print('up, left, down, right: %s, %s, %s, %s' %(up, left, down, right))
    area = [0, 0, 0, 0, 0]
    test = [[0 for i in range(N)] for j in range(N)]
    for i in range(up[0], left[0] + 1):
        y = i, x = up[1]
        test[y][x] = 5
        x -= 1
    for i in range(left[0], down[0] + 1):
        y = i, x = left[1]
        test[y][x] = 5
        
    for i in range(N):
        print(test[i])
    print('area: %s' %area)
    return max(area) - min(area)


if __name__ == "__main__":
    main()
