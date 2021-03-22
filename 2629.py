import sys


def main():
    wCnt = int(sys.stdin.readline())
    wList = list(map(int, sys.stdin.readline().split()))
    bCnt = int(sys.stdin.readline())
    bList = list(map(int, sys.stdin.readline().split()))
    dp = [[0 for j in range(50001)] for i in range(wCnt + 1)]
    for i in range(1, wCnt + 1): # i: dp의 행
        w = wList[i - 1] # 지금 무게
        dp[i][w] = 1
        for j in range(50001):
            if dp[i - 1][j]: # i - 1행에서 무게 j 인 값이 가능할 때
                dp[i][j] = dp[i - 1][j]
                dp[i][abs(w - j)] = 1
                dp[i][j + w] = 1
    for i in range(bCnt):
        bW = bList[i]
        if dp[wCnt][bW]:
            print('Y', end=' ')
        else:
            print('N', end=' ')


if __name__ == '__main__':
    main()
