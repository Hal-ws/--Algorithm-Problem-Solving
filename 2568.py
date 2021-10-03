import sys
from bisect import bisect_left


def main():
    N = int(sys.stdin.readline())
    nList = []
    for _ in range(N):
        nList.append(list(map(int, sys.stdin.readline().split())))
    nList.sort()
    LIS = [nList[0][1]]
    idxList = [0]
    ansLines = set()
    for i in range(1, N):
        num = nList[i][1]
        if num > LIS[-1]:
            LIS.append(num)
            idxList.append(len(LIS) - 1)
        else:
            idx = bisect_left(LIS, num)
            LIS[idx] = num
            idxList.append(idx)
    pIdx = len(LIS) - 1
    ansCnt = 0
    for i in range(N - 1, -1, -1):
        if idxList[i] == pIdx:
            ansLines.add(nList[i][0])
            ansCnt += 1
            pIdx -= 1
    print(N - ansCnt)
    for i in range(N):
        if nList[i][0] not in ansLines:
            print(nList[i][0])


if __name__ == "__main__":
    main()
