import sys
sys.setrecursionlimit(pow(10, 8))


def main():
    global inOrder, postOrder
    N = int(sys.stdin.readline())
    inOrder = list(map(int, sys.stdin.readline().split()))
    postOrder = list(map(int, sys.stdin.readline().split()))
    printPre(0, N - 1, 0, N - 1)


def printPre(sIn, eIn, sPost, ePost): # 각각 In, Post order가 시작 / 끝나는 index 표시
    global inOrder, postOrder
    tmpIn, tmpPost = inOrder[sIn:eIn + 1], postOrder[sPost:ePost + 1]
    l = len(tmpIn)
    if len(tmpPost) == 0:
        tmpIn, tmpPost = [], []
        return
    root = tmpPost[-1]
    rIdx = tmpIn.index(root)
    tmpIn, tmpPost = [], []
    print(root, end=' ')
    if len(tmpPost) == 1:
        return
    nxtSIn, nxtEIn = sIn, sIn + rIdx - 1
    nxtSPost, nxtEPost = sPost, sPost + rIdx - 1
    printPre(nxtSIn, nxtEIn, nxtSPost, nxtEPost)
    nxtSIn, nxtEIn = sIn + rIdx + 1, sIn + l - 1
    nxtSPost, nxtEPost = sPost + rIdx, sPost + l - 2
    printPre(nxtSIn, nxtEIn, nxtSPost, nxtEPost)


if __name__ == '__main__':
    main()
