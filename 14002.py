def main():
    N = int(input())
    nums = list(map(int, input().split()))
    dp = [[nums[0], 1]]
    ansList = [[nums[0]]] + [0] * (N - 1)
    for i in range(1, N):
        dp.append(getVal(dp, nums, ansList, i))
    ansIdx = 0
    ansLen = len(ansList[0])
    for i in range(1, N):
        tempLen = len(ansList[i])
        if tempLen >= ansLen:
            ansIdx = i
            ansLen = tempLen
    la = len(ansList[ansIdx])
    print(la)
    for i in range(la):
        print(ansList[ansIdx][i], end=' ')


def getVal(dp, nums, ansList, idx):
    lastPoint = [0, 0]  ## LAST 포인트가 되는 길이, index 저장
    for i in range(idx - 1, -1, -1):
        if dp[i][0] < nums[idx]:
            temp = dp[i][1]
            if temp > lastPoint[0]:
                lastPoint = [temp, i]
    if lastPoint == [0, 0]:
        ansList[idx] = [nums[idx]]
        return [nums[idx], 1]
    else:
        ansList[idx] = ansList[lastPoint[1]] + [nums[idx]]
        return [nums[idx], dp[lastPoint[1]][1] + 1]


if __name__ == "__main__":
    main()
