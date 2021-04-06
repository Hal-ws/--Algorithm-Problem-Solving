import sys
from math import inf


def main():
    nList = list(map(int, sys.stdin.readline().split()))
    dp = [[[inf for k in range(5)] for j in range(5)] for i in range(len(nList) - 1)]
    answer = inf
    dp[0][nList[0]][0] = 2
    dp[0][0][nList[0]] = 2
    for i in range(1, len(nList) - 1):
        num = nList[i]
        for j in range(5):
            for k in range(5):
                if dp[i - 1][j][k] != inf: # 해당 dp값에 도착한 크기가 있으면
                    if k != num: # dp[i][num][k]에 저장가능
                        p = dp[i - 1][j][k] + getForce(j, num)
                        if p < dp[i][num][k]:
                            dp[i][num][k] = p
                    if j != num: # dp[i][j][num]에 저장가능
                        p = dp[i - 1][j][k] + getForce(k, num)
                        if p < dp[i][j][num]:
                            dp[i][j][num] = p
    for j in range(5):
        for k in range(5):
            if dp[-1][j][k] != inf and dp[-1][j][k] < answer:
                answer = dp[-1][j][k]
    print(answer)


def getForce(a, b):
    if a == 0 or b == 0 and a != b:
        return 2
    if a == b:
        return 1
    if a == 1:
        if b == 2 or b == 4:
            return 3
        if b == 3:
            return 4
    if a == 2:
        if b == 1 or b == 3:
            return 3
        if b == 4:
            return 4
    if a == 3:
        if b == 2 or b == 4:
            return 3
        if b == 1:
            return 4
    if a == 4:
        if b == 1 or b == 3:
            return 3
        if b == 2:
            return 4


if __name__ == '__main__':
    main()
