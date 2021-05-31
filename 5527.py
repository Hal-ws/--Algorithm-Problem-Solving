import sys


def main():
    global N, nList
    N = int(sys.stdin.readline())
    nList = list(map(int, sys.stdin.readline().split()))
    std1 = [0 for i in range(N)]
    std2 = [0 for i in range(N)]
    for i in range(N):
        if i % 2 == 0:
            std1[i] = 1
            std2[i] = 0
        else:
            std1[i] = 0
            std2[i] = 1
    print(max(getLen(nList, std1, N), getLen(nList, std2, N)))


def getLen(nList, stdList, N):
    dp = [0] * N
    result = 0
    if stdList[0] == nList[0]:
        dp[0] = 1
    for i in range(1, N):
        if stdList[i] == nList[i]:
            dp[i] = dp[i - 1] + 1
    cLen = 1
    zFlag = 0 # dp[i - 1]의 값이 0임
    if dp[0] == 0:
        zFlag = 1
    for i in range(1, N):
        if dp[i] == 0:
            if zFlag:
                cLen += 1
            else:
                cLen = dp[i - 1] + 1
            zFlag = 1
        else:
            cLen += 1
            zFlag = 0
        if cLen > result:
            result = cLen
    return result


if __name__ == '__main__':
    main()
