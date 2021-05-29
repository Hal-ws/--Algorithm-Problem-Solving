import sys


def main():
    s, d, k, h = map(int, sys.stdin.readline().split())
    dp = [[[[0 for i in range(51)] for ii in range(51)] for iii in range(51)] for iiii in range(51)]
    dp[0][0][0][0] = 1
    divide = 1000000007
    for sIdx in range(s):
        for dIdx in range(d + 1):
            for kIdx in range(k + 1):
                for hIdx in range(h + 1):
                    dp[sIdx][dIdx][kIdx][hIdx] = dp[sIdx][dIdx][kIdx][hIdx] % divide
                    curVal = dp[sIdx][dIdx][kIdx][hIdx]
                    if dIdx < d:
                        dp[sIdx + 1][dIdx + 1][kIdx][hIdx] += curVal
                        if hIdx < h:
                            dp[sIdx + 1][dIdx + 1][kIdx][hIdx + 1] += curVal
                        if kIdx < k:
                            dp[sIdx + 1][dIdx + 1][kIdx + 1][hIdx] += curVal
                            if hIdx < h:
                                dp[sIdx + 1][dIdx + 1][kIdx + 1][hIdx + 1] += curVal
                    if kIdx < k:
                        dp[sIdx + 1][dIdx][kIdx + 1][hIdx] += curVal
                        if hIdx < h:
                            dp[sIdx + 1][dIdx][kIdx + 1][hIdx + 1] += curVal
                    if hIdx < h:
                        dp[sIdx + 1][dIdx][kIdx][hIdx + 1] += curVal
    print(dp[s][d][k][h] % divide)


if __name__ == '__main__':
    main()
