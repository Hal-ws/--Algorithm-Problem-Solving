def main():
    N = int(input())
    nums = list(map(int, input().split()))
    dp = [[nums[0], 1]]
    ansList = [[nums[0]]] + [0] * (N - 1)
    for i in range(1, N):
        dp.append(getVal(dp, nums, ansList, i))
    print(dp)
    print(ansList)


def getVal(dp, nums, ansList, idx):
    lastPoint = [0, 0] ## LAST 포인트가 되는 길이, index 저장
    for i in range(idx - 1, -1, -1):
        if dp[i][0] < nums[idx]:
            length = dp[i][1] + 1
            temp = dp[i][1]
            if temp > lastPoint[0]:
                lastPoint = [temp, i]


if __name__ == "__main__":
    main()
