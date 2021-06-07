import sys


def main():
    N = int(sys.stdin.readline())
    sys.setrecursionlimit(pow(10, 6))
    nodeInfo = [[0, 0, 0] for i in range(N + 1)] # left 갯수, right 갯수, level
    nodePos = [[0, 0] for i in range(N + 1)] # node의 level, x값
    tree = [None]
    for i in range(N):
        node, left, right = map(int, sys.stdin.readline().split())
        tree.append([left, right])
    nodeInfo[1][2] = 1
    cntLeaves(1, tree, nodeInfo, 1)
    getPos(1, 1, N, nodePos, nodeInfo, tree, 1)
    maxLevel = nodePos[-1][0]
    ansLevel = 0
    maxWidth = 0
    lvlList = [[] for i in range(maxLevel + 1)]
    for i in range(len(nodePos)):
        level, x = nodePos[i][0], nodePos[i][1]
        lvlList[level].append(x)
    for level in range(1, len(lvlList)):
        lvlList[level].sort()
        if lvlList[level][-1] - lvlList[level][0] + 1 > maxWidth:
            maxWidth = lvlList[level][-1] - lvlList[level][0] + 1
            ansLevel = level
    print(nodePos)
    print(nodeInfo)
    print('%s %s' %(ansLevel, maxWidth))


def getPos(node, lBound, rBound, nodePos, nodeInfo, tree, level):
    nodePos[node][0] = level
    left, right = tree[node][0], tree[node][1]
    x = lBound + nodeInfo[node][0]
    nodePos[node][1] = x
    if left != -1: # 왼쪽 노드 구하러감
        getPos(left, lBound, x - 1, nodePos, nodeInfo, tree, level + 1)
    if right != -1: # 오른쪽 노드 구하러감
        getPos(right, x + 1, rBound, nodePos, nodeInfo, tree, level + 1)


def cntLeaves(node, tree, nodeInfo, level):
    left, right = tree[node][0], tree[node][1]
    flag1, flag2 = 0, 0
    if right != -1:
        nodeInfo[right][2] = level + 1
        cnt1 = cntLeaves(right, tree, nodeInfo, level + 1)
        nodeInfo[node][1] = cnt1
        flag1 = 1
    if left != -1:
        nodeInfo[left][2] = level + 1
        cnt2 = cntLeaves(left, tree, nodeInfo, level + 1)
        nodeInfo[node][0] = cnt2
        flag2 = 1
    if flag1 == flag2 == 1:
        return cnt1 + cnt2 + 1
    if flag1 == 1:
        return cnt1 + 1
    if flag2 == 1:
        return cnt2 + 1
    if left == -1 and right == -1:
        return 1


if __name__ == '__main__':
    main()
