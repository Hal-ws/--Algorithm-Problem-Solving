import sys


def main():
    global N, fList
    N = int(sys.stdin.readline())
    fList = [0] * 21
    for i in range(21):
        fList[i] = factorial(i)
    inputList= list(map(int, sys.stdin.readline().split()))
    if inputList[0] == 1:
        nList1 = [i + 1 for i in range(N)]
        case1(nList1, inputList[1], [])
    else:
        nList2 = [inputList[i] for i in range(1, len(inputList))]
        case2(nList2, fList[N])


def case1(nList, cnt, ans): #nList에서 cnt번째로 오는 것을 구함
    global N, fList
    nList = sorted(nList)
    if len(ans) == N:
        for i in range(N):
            print(ans[i], end=' ')
        return 0
    tmpCnt = 0
    for i in range(len(nList)):
        tmpCnt += fList[len(nList) - 1]
        if cnt <= tmpCnt:
            tmpCnt -= fList[len(nList) - 1]
            ans.append(nList[i])
            del nList[i]
            return case1(nList, cnt - tmpCnt, ans)


def case2(nList, cnt):
    global N, fList
    if len(nList) == 1:
        print(cnt)
        return
    tmp = [nList[i] for i in range(len(nList))]
    tmp = sorted(tmp)
    idx = tmp.index(nList[0]) + 1 # 몇번째로 큰 수인지 결정
    nCnt = cnt - (len(nList) - idx) * fList[len(nList) - 1]
    del nList[0]
    return case2(nList, nCnt)


def factorial(n):
    global fList
    if n == 0:
        return 1
    return fList[n - 1] * n


if __name__ == '__main__':
    main()
