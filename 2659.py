import sys
from itertools import product
from collections import deque


def main():
    numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    stdList = list(map(int, sys.stdin.readline().split()))
    clockList = getclockList(list(product(numList, repeat=4)))
    stdClock = min(stdList[0] * pow(10, 3) + stdList[1] * pow(10, 2) + stdList[2] * pow(10, 1) + stdList[3] * pow(10, 0),
                   stdList[1] * pow(10, 3) + stdList[2] * pow(10, 2) + stdList[3] * pow(10, 1) + stdList[0] * pow(10, 0),
                   stdList[2] * pow(10, 3) + stdList[3] * pow(10, 2) + stdList[0] * pow(10, 1) + stdList[1] * pow(10, 0),
                   stdList[3] * pow(10, 3) + stdList[0] * pow(10, 2) + stdList[1] * pow(10, 1) + stdList[2] * pow(10, 0))
    cnt = 1
    for i in range(1, len(clockList)):
        if clockList[i] == 1:
            if i == stdClock:
                print(cnt)
                break
            else:
                cnt += 1


def getclockList(nList):
    clockList = [0] * (9 * 9 * 9 * 9 * 4 + 1)
    for i in range(len(nList)):
        tmpQ = deque()
        for j in range(4):
            tmpQ.append(nList[i][j])
        clockNum = 10000
        for j in range(4):
            tmpQ.appendleft(tmpQ.pop())
            tmpVal = tmpQ[0] * pow(10, 3) + tmpQ[1] * pow(10, 2) + tmpQ[2] * pow(10, 1) + tmpQ[3] * pow(10, 0)
            if tmpVal < clockNum:
                clockNum = tmpVal
        clockList[clockNum] = 1
    return clockList


if __name__ == '__main__':
    main()
