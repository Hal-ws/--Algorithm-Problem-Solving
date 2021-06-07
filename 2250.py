import sys


def main():
    N = int(sys.stdin.readline())
    nodeInfo = [[0, 0, 0] for i in range(N + 1)] # left 갯수, right 갯수, level
    tree = [None]
    for i in range(N):
        node, left, right = map(int, sys.stdin.readline().split())
        tree.append([left, right])
    nodeInfo[1][2] = 1
    cntLeaves(1, tree, nodeInfo, 1)
    print(nodeInfo)
    return 0


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
