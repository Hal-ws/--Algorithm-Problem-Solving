import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    nList = list(map(int, sys.stdin.readline().split()))
    left, right = 0, 10000
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if chkPossible(nList, N, M, mid):
            right = mid - 1
            ans = mid
        else:
            left = mid + 1
    print(ans)


def chkPossible(nList, N, M, mid):
    sliceCnt = 1
    minVal, maxVal = None, None
    i = 0
    while i < N:
        num = nList[i]
        if minVal == maxVal == None:
            minVal = num
        elif maxVal == None:
            maxVal = num
            minVal, maxVal = min(minVal, maxVal), max(minVal, maxVal)
        else:
            if num < minVal:
                minVal = num
            if num > maxVal:
                maxVal = num
        if minVal != None and maxVal != None:
            if maxVal - minVal > mid:
                minVal, maxVal = None, None
                sliceCnt += 1
            else:
                i += 1
            if sliceCnt > M:
                return 0
        else:
            i += 1
    return 1


if __name__ == "__main__":
    main()
