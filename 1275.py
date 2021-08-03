import sys


def main():
    N, Q = map(int, sys.stdin.readline().split())
    nList = list(map(int, sys.stdin.readline().split()))
    layer = 1
    if N > 1:
        while 1:
            if pow(2, layer - 1) < N <= pow(2, layer):
                layer += 1
                break
            layer += 1
    segTree = [0 for i in range(pow(2, layer))]
    coverIdx = [[0, 0] for i in range(pow(2, layer))]
    sIdx = pow(2, layer - 1)
    for i in range(sIdx, pow(2, layer)):
        coverIdx[i] = [i, i]
    for i in range(sIdx - 1, 0, -1):
        left, right = i * 2, i * 2 + 1
        coverIdx[i][0] = coverIdx[left][0]
        coverIdx[i][1] = coverIdx[right][1]
    print(coverIdx)

    for i in range(N):
        segTree[sIdx + i] = nList[i]
    for _ in range(Q):
        x, y, a, b = map(int, sys.stdin.readline().split())
        x, y, a = x - 1, y - 1, a - 1
        x, y, a, b = min(sIdx + x, sIdx + y), max(sIdx + x, sIdx + y), sIdx + a, b
        print(getSum(segTree, x, y))
        change(segTree, a, b)
    return 0


def change(tree, a, b): #a번째 수를 b로 변경

    return 0


def getSum(tree, a, b):
    return 0


if __name__ == "__main__":
    main()
