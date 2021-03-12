import sys
sys.setrecursionlimit(pow(10, 8))


def main():
    global inOrder, postOrder, inIdx, postIdx
    N = int(sys.stdin.readline())
    inIdx, postIdx = {}, {}
    inOrder = list(map(int, sys.stdin.readline().split()))
    postOrder = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        inIdx[inOrder[i]] = i
        postIdx[postOrder[i]] = i
    printPre(0, N - 1, 0, N - 1)


def printPre(sIn, eIn, sPost, ePost): # 각각 In, Post order가 시작 / 끝나는 index 표시
    global inOrder, postOrder, inIdx, postIdx
    if sIn > eIn:
        return
    root = postOrder[ePost]
    print(root, end=' ')
    rIdx1 = inIdx[root]
    l1, l2 = rIdx1 - sIn, eIn - rIdx1
    if sPost == ePost:
        return
    nxtSIn, nxtEIn = sIn, rIdx1 - 1
    nxtSPost, nxtEPost = sPost, sPost + l1 - 1
    printPre(nxtSIn, nxtEIn, nxtSPost, nxtEPost)
    nxtSIn, nxtEIn = rIdx1 + 1, eIn
    nxtSPost, nxtEPost = ePost - l2, ePost - 1
    printPre(nxtSIn, nxtEIn, nxtSPost, nxtEPost)


if __name__ == '__main__':
    main()
