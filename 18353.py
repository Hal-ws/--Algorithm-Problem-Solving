import sys


def main():
    N = int(sys.stdin.readline())
    nList = [10000001] + list(map(int, sys.stdin.readline().split()))
    maxLen = 1
    dp = [0 for i in range(N + 1)] # i번째 nList로 끝나는 최대 길이 저장
    for i in range(1, N + 1): #
        for j in range(i - 1, -1, -1):
            if nList[i] < nList[j]: # 내림차순 가능
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    if dp[i] > maxLen:
                        maxLen = dp[i]
    print(N - maxLen)


if __name__ == "__main__":
    main()
