import sys

def main():
    N = int(sys.stdin.readline())
    schedule = [0] * (N + 1)
    for i in range(1, N + 1):
        schedule[i] = list(map(int, sys.stdin.readline().split()))
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = maxreward(schedule, dp, i)
    print(dp[N])


def maxreward(schedule, dp, endday):
    maxVal = 0
    startdays = []
    for i in range(endday, 0, - 1):
        if schedule[i][0] + i - 1 <= endday:
            startdays.append(i)
    ls = len(startdays)
    for i in range(ls):
        temp = dp[startdays[i] - 1] + schedule[startdays[i]][1]
        if temp >= maxVal:
            maxVal = temp
    return maxVal


if __name__ == "__main__":
    main()
