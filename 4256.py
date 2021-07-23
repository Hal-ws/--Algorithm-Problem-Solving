import sys


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        getAns()


def getAns():
    n = int(sys.stdin.readline())
    global tree, preOrder, preIdx, inOrder, inIdx
    preOrder = list(map(int, sys.stdin.readline().split()))
    inOrder = list(map(int, sys.stdin.readline().split()))
    preIdx = [None] * (n + 1)
    inIdx = [None] * (n + 1)
    tree = [[None, None] for i in range(n + 1)]
    for i in range(n):
        node = preOrder[i]
        preIdx[node] = i
        node = inOrder[i]
        inIdx[node] = i
    makeTree(0, n - 1, 0, n - 1)
    postOrder(tree, preOrder[0])
    print()


def makeTree(preLeft, preRight, inLeft, inRight):
    rootNode = preOrder[preLeft]
    pIdx = preIdx[rootNode]
    iIdx = inIdx[rootNode] # inOrder 내의 rootNode의 idx를 구함
    leftLen, rightLen = iIdx - inLeft, inRight - iIdx
    if leftLen > 0: #왼쪽 tree를 만들게 있음
        leftRoot = preOrder[pIdx + 1] # 왼쪽 트리의 root node
        tree[rootNode][0] = leftRoot
        makeTree(preIdx[rootNode] + 1, preIdx[rootNode] + leftLen, inLeft, inIdx[rootNode] - 1)
    if rightLen > 0: #오른쪽 tree를 만들게 있음
        rightRoot = preOrder[pIdx + leftLen + 1]
        tree[rootNode][1] = rightRoot
        makeTree(preIdx[rootNode] + leftLen + 1, preRight, inIdx[rootNode] + 1, inRight)


def postOrder(tree, node):
    left, right = tree[node][0], tree[node][1]
    if left != None:
        postOrder(tree, left)
    if right != None:
        postOrder(tree, right)
    print(node, end=' ')


if __name__ == '__main__':
    main()
