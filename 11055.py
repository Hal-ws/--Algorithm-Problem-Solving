def main():
    N = int(input())
    nums = list(map(int, input().split()))
    dp = [[nums[0], nums[0]]] ## 크기, 합
    for i in range(1, N):
        dp.append(getdp(dp, nums, i))
    ans = 0
    for i in range(N):
        if dp[i][1] >= ans:
            ans = dp[i][1]
    print(ans)


def getdp(dp, nums, idx):
    maxPoint = [0, 0] ## 합친 값 / index
    for i in range(idx - 1, -1, -1):
        if dp[i][0] < nums[idx]:
            temp = dp[i][1]
            if temp > maxPoint[0]:
                maxPoint = [temp, i]
    if maxPoint == [0, 0]:
        return [nums[idx], nums[idx]]
    else:
        return [nums[idx], dp[maxPoint[1]][1] + nums[idx]]


if __name__ == "__main__":
    main()
