import sys
from itertools import combinations


def main():
    global rightDic
    N, S = map(int, sys.stdin.readline().split())
    cnt = 0
    nList = list(map(int, sys.stdin.readline().split()))
    leftNum, rightNum = nList[:N // 2], nList[N // 2:]
    rightDic = {}
    leftList = getcase(leftNum, 0)
    rightList = getcase(rightNum, 1)
    for i in range(len(leftList)):
        if leftList[i] == S:
            cnt += 1
    for i in range(len(rightList)):
        if rightList[i] == S:
            cnt += 1
    for i in range(len(leftList)):
        val = leftList[i]
        if rightDic.get(S - val) != None:
            cnt += rightDic[S - val]
    print(cnt)


def getcase(nList, flag):
    global rightDic
    val = []
    for l in range(1, len(nList) + 1):
        cases = list(combinations(nList, l))
        for i in range(len(cases)):
            tmpSum = sum(cases[i])
            val.append(tmpSum)
            if flag:
                if rightDic.get(tmpSum) == None:
                    rightDic[tmpSum] = 1
                else:
                    rightDic[tmpSum] += 1
    return val


if __name__ == '__main__':
    main()
