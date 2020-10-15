def main():
    N = int(input())
    nums = list(map(int, input().split()))
    dp = [[nums[0], 1]]
    ansList = [nums[0]]
    for i in range(1, N):
        dp.append(getVal(dp, nums, ansList, i))
    print(dp)


def getVal(dp, nums, ansList, idx):
    findflag = 0
    for i in range(idx - 1, -1, -1):
        if dp[i][0] < nums[idx]:
            length = dp[i][1] + 1
            findflag = 1
            break
    if findflag:
        return [nums[idx], length]
    else:
        return [nums[idx], 1]


if __name__ == "__main__":
    main()
