import sys
from math import sqrt


def main():
    N = int(sys.stdin.readline())
    dp = [0 for i in range(50001)]
    for i in range(int(sqrt(50001) + 1)):
        dp[i * i] = 1
    for i in range(2, 50001):
        if dp[i] == 0:
            minVal = 5
            for j in range(1, i + 1):
                idx = i - j * j
                if idx <= 0:
                    break
                if dp[idx] < minVal:
                    minVal = dp[idx]
            dp[i] = minVal + 1
    print(dp[N])


if __name__ == "__main__":
    main()
