def main():
    N = int(input())
    nums = list(map(int, input().split()))
    dp = [[nums[0], 1]]
    for i in range(1, N):
        dp.append(getVal(dp, nums, i))
    print(dp)


def getVal(dp, nums, idx):
    findflag = 0
    for i in range(idx - 1, -1, -1):
        if dp[i][0] < nums[idx]:
            num = dp[i][0]
            length = dp[i][1] + 1
            findflag = 1
            break
    if findflag:
        return [num, length]
    else:
        return [nums[idx], 1]


if __name__ == "__main__":
    main()
