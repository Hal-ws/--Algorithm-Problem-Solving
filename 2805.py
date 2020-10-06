import sys


def cutTrees(trees, height):
    sumOfTrees = 0
    for i in range(len(trees)):
        cutted = trees[i] - height
        if cutted <= 0:
            cutted = 0
        sumOfTrees += cutted
    return sumOfTrees


N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
lowHeight = 0
highHeight = max(trees)

while lowHeight < highHeight:
    mid = (lowHeight + highHeight) // 2
    bringTree = cutTrees(trees, mid)
    if bringTree == M:
        break
    elif bringTree > M:
        lowHeight = mid + 1
    else:
        highHeight = mid - 1

if bringTree == M:
    print(mid)
elif bringTree < M:
    while bringTree < M:
        mid -= 1
        bringTree = cutTrees(trees, mid)
    print(mid)
elif bringTree > M and cutTrees(trees, mid + 1) >= M:
    print(mid + 1)
else:
    print(mid)
