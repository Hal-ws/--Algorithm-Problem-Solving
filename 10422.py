import sys


def main():
    T = int(sys.stdin.readline())
    dp = [0] * 2501
    dp[0] = 1
    for i in range(1, 2501):
        tmp = 0
        for j in range(1, i + 1):
            tmp += dp[i - j] * dp[j - 1]
        dp[i] = tmp % 1000000007
    for i in range(T):
        L = int(sys.stdin.readline())
        if L % 2 == 0:
            print(dp[L // 2])
        else:
            print(0)


if __name__ == '__main__':
    main()
