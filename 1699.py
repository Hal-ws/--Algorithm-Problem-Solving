import math


def main():
    N = int(input())
    dp = [0]
    for i in range(1, N + 1):
        if math.sqrt(i) % 1 == 0:
            dp.append(1)
        else:
            minAns = 100000
            for j in range(1, int(math.sqrt(i)) + 1):
                if i == 100000:
                    print("dp[j * j] : %s dp[i - j * j]: %s" % (dp[j * j], dp[i - j * j]))
                if dp[j * j] + dp[i - j * j] <= minAns:
                    minAns = dp[j * j] + dp[i - j * j]
            dp.append(minAns)
    print(dp[N])


if __name__ == "__main__":
    main()
