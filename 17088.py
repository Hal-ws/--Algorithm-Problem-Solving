import sys
from copy import deepcopy


def main():
    global N
    N = int(sys.stdin.readline())
    nList = list(map(int, sys.stdin.readline().split()))
    answer = pow(10, 5) + 1
    dv = [-1, 0, 1]
    if N == 1 or N == 2:
        answer = 0
    else:
        for i in range(3):
            for j in range(3):
                tmpList = deepcopy(nList)
                tmpList[0], tmpList[1] = tmpList[0] + dv[i], tmpList[1] + dv[j]
                tmpAns = makeSeries(tmpList[1] - tmpList[0], tmpList)
                if tmpList[0] != nList[0]:
                    tmpAns += 1
                if tmpList[1] != nList[1]:
                    tmpAns += 1
                if tmpAns < answer:
                    answer = tmpAns
    if answer == pow(10, 5) + 1:
        print(-1)
    else:
        print(answer)


def makeSeries(d, nList):
    global N
    result = 0
    for i in range(2, N):
        diff = nList[i] - nList[i - 1]
        if diff == d + 1 or diff == d - 1:
            result += 1
            nList[i] = nList[i - 1] + d
        elif diff != d:
            return pow(10, 5) + 1
    return result


if __name__ == '__main__':
    main()
