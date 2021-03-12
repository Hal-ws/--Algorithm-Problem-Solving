import sys
sys.setrecursionlimit(pow(10, 8))


def main():
    global inOrder, postOrder, inIdx
    N = int(sys.stdin.readline())
    inIdx = {}
    inOrder = list(map(int, sys.stdin.readline().split()))
    postOrder = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        inIdx[inOrder[i]] = i
    printPre(0, N - 1, 0, N - 1)


def printPre(sIn, eIn, sPost, ePost):
    global inOrder, postOrder, inIdx
    if sIn > eIn:
        return
    root = postOrder[ePost]
    print(root, end=' ')
    rIdx1 = inIdx[root]
    l1, l2 = rIdx1 - sIn, eIn - rIdx1
    if sPost == ePost:
        return
    printPre(sIn, rIdx1 - 1, sPost, sPost + l1 - 1)
    printPre(rIdx1 + 1, eIn, ePost - l2, ePost - 1)


if __name__ == '__main__':
    main()
