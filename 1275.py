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
    coverNode = [[0, 0] for i in range(pow(2, layer))]
    sIdx = pow(2, layer - 1)
    for i in range(N):
        segTree[sIdx + i] = nList[i]
    for i in range(sIdx, pow(2, layer)):
        coverNode[i] = [i, i]
    for i in range(sIdx - 1, 0, -1):
        left, right = i * 2, i * 2 + 1
        coverNode[i][0] = coverNode[left][0]
        coverNode[i][1] = coverNode[right][1]
        segTree[i] = segTree[left] + segTree[right]
    for _ in range(Q):
        x, y, a, b = map(int, sys.stdin.readline().split())
        x, y, a = x - 1, y - 1, a - 1
        x, y, a, b = min(sIdx + x, sIdx + y), max(sIdx + x, sIdx + y), sIdx + a, b
        print(getSum(segTree, coverNode, x, y, 1))
        change(segTree, a, b)
    return 0


def getSum(segTree, coverNode, a, b, node): # a부터 b까지 더한 값을 return함. node는 현재 node
    bLeft, bRight = coverNode[node][0], coverNode[node][1]
    if a == bLeft and b == bRight:
        return segTree[node]
    leftNode, rightNode = node * 2, node * 2 + 1
    val1, val2 = 0, 0
    if coverNode[leftNode][0] <= a <= coverNode[leftNode][1]:
        if b > coverNode[leftNode][1]:
            val1 = getSum(segTree, coverNode, a, coverNode[leftNode][1], leftNode)
        else:
            val1 = getSum(segTree, coverNode, a, b, leftNode)
    if coverNode[rightNode][0] <= b <= coverNode[rightNode][1]:
        if a < coverNode[rightNode][0]:
            val2 = getSum(segTree, coverNode, coverNode[rightNode][0], b, rightNode)
        else:
            val2 = getSum(segTree, coverNode, a, b, rightNode)
    return val1 + val2


def change(segTree, idx, b): #a번째 수를 b로 변경
    diff = b - segTree[idx]
    while idx >= 1:
        segTree[idx] += diff
        idx = idx // 2


if __name__ == "__main__":
    main()
