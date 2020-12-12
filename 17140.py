import sys


def main():
    r, c, k = map(int, sys.stdin.readline().split())
    board = []
    for i in range(3):
        board.append(list(map(int, sys.stdin.readline().split())))
    t = 0
    flag = 0
    while t <= 100:
        height = len(board)
        wide = len(board[0])
        if 0 <= r - 1 < height and 0 <= c - 1 < wide and board[r - 1][c - 1] == k:
            flag = 1
            break
        if height >= wide:
            R(board, height, wide)
        else:
            board = C(board, height, wide)
        t += 1
    if flag:
        print(t)
    else:
        print(-1)


def R(board, height, wide):
    maxLen = 0
    for i in range(height):
        new = sorted(board[i])
        for j in range(wide):
            if new[j] != 0:
                tmpLen = 2
                tmpList = [new[j], 1]
                idx = j
                break
        for j in range(idx + 1, wide):
            if new[j] == tmpList[tmpLen - 2]:
                tmpList[tmpLen - 1] += 1
            else:
                tmpList.append(new[j])
                tmpList.append(1)
                tmpLen += 2
                if tmpLen >= 100:
                    break
        tmpList = listsort(tmpList, tmpLen)
        board[i] = tmpList
        if maxLen <= tmpLen:
            maxLen = tmpLen
    for i in range(height):
        board[i] += [0] * (maxLen - len(board[i]))


def C(board, height, wide):
    newboard = []
    maxLen = 0
    for j in range(wide):
        new = []
        for i in range(height):
            new.append(board[i][j])
        new.sort()
        for i in range(height):
            if new[i] != 0:
                tmpLen = 2
                tmpList = [new[i], 1]
                idx = i
                break
        for i in range(idx + 1, height):
            if new[i] == tmpList[tmpLen - 2]:
                tmpList[tmpLen - 1] += 1
            else:
                tmpList.append(new[i])
                tmpList.append(1)
                tmpLen += 2
                if tmpLen >= 100:
                    break
        tmpList = listsort(tmpList, tmpLen)
        newboard.append(tmpList)
        if maxLen <= tmpLen:
            maxLen = tmpLen

    for i in range(len(newboard)):
        newboard[i] += [0] * (maxLen - len(newboard[i]))
    result = [[0 for j in range(len(newboard))] for i in range(maxLen)]
    for j in range(len(newboard)):
        for i in range(maxLen):
            result[i][j] = newboard[j][i]
    return result


def listsort(inputlist, l):
    tmp = []
    for i in range(0, l, 2):
        tmp.append([inputlist[i + 1], inputlist[i]]) ## 등장횟수, 숫자
    tmp.sort()
    result = []
    for i in range(l // 2):
        tmp[i][0], tmp[i][1] = tmp[i][1], tmp[i][0]
        result += tmp[i]
    return result


if __name__ == "__main__":
    main()
