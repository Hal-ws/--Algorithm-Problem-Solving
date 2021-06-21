import sys


def main():
    N, M, K = map(int, sys.stdin.readline().split())
    i = 0
    while 1:
        if pow(2, i) >= N:
            tree = [0] * pow(2, i + 1)
            coverIdx = [[-1, -1] for j in range(pow(2, i + 1))]
            sIdx = pow(2, i)
            break
        i += 1
    for i in range(N):
        val = int(sys.stdin.readline())
        tree[sIdx + i] = val
    for i in range(sIdx, len(coverIdx)):
        coverIdx[i] = [i, i]
    for idx in range(len(tree) - 1, 1, -1):
        tree[idx // 2] += tree[idx]
        if idx % 2 == 1:
            coverIdx[idx // 2][1] = coverIdx[idx][1]
        else:
            coverIdx[idx // 2][0] = coverIdx[idx][0]
    for i in range(M + K):
        a, b, c = map(int, sys.stdin.readline().split())
        if a == 1:
            changeNum(sIdx + b - 1, c - tree[sIdx + b - 1], tree)
        else:
            print(getSum(sIdx + b - 1, sIdx + c - 1, tree, 1, coverIdx, len(tree)))


def changeNum(idx, diff, tree):
    while idx >= 1:
        tree[idx] += diff
        idx = idx // 2


def getSum(b, c, tree, cIdx, coverIdx, treeL):
    start, end = coverIdx[cIdx][0], coverIdx[cIdx][1]
    result, add1, add2 = 0, 0, 0
    if b <= start <= c and b <= end <= c:
        result = tree[cIdx]
    else:
        if cIdx * 2 + 1 < treeL:
            nxtCover = coverIdx[cIdx * 2 + 1]
            if b <= nxtCover[0] <= c or b <= nxtCover[1] <= c or nxtCover[0] <= b <= nxtCover[1] or nxtCover[0] <= c <= nxtCover[1]:
                add1 = getSum(b, c, tree, cIdx * 2 + 1, coverIdx, treeL)
            nxtCover = coverIdx[cIdx * 2]
            if b <= nxtCover[0] <= c or b <= nxtCover[1] <= c or nxtCover[0] <= b <= nxtCover[1] or nxtCover[0] <= c <= nxtCover[1]:
                add2 = getSum(b, c, tree, cIdx * 2, coverIdx, treeL)
    return result + add1 + add2


if __name__ == '__main__':
    main()
