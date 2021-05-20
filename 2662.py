import sys
from copy import deepcopy


def main():
    N, M = map(int, sys.stdin.readline().split())
    rTable = [[0 for i in range(M)]] # reward table
    dp = [[[0, []] for j in range(M)] for i in range(N + 1)]
    for i in range(N):
        tmp = list(map(int, sys.stdin.readline().split()))
        tmp = tmp[1:]
        rTable.append(tmp)
    for i in range(N + 1):
        culM = i # 사용 누적 금액
        dp[culM][0] = [rTable[i][0], [i]]
    for cIdx in range(M - 1): # company의 index
        for usedM in range(N + 1): # 누적이 usedM만큼 사용
            rSum = dp[usedM][cIdx][0] # 지금까지 얻은 reward
            path = dp[usedM][cIdx][1]
            for usingM in range(N - usedM + 1): # 새로 usingM만큼 더 써줌
                add = rTable[usingM][cIdx + 1]
                if rSum + add > dp[usedM + usingM][cIdx + 1][0]:
                    nPath = deepcopy(path)
                    nPath.append(usingM)
                    dp[usedM + usingM][cIdx + 1][0] = rSum + add
                    dp[usedM + usingM][cIdx + 1][1] = nPath
    maxR = 0
    for i in range(N + 1):
        if dp[i][M - 1][0] > maxR:
            maxR = dp[i][M - 1][0]
            ansList = dp[i][M - 1][1]
    print(maxR)
    for m in ansList:
        print(m, end=' ')


if __name__ == '__main__':
    main()
