import sys
from collections import deque


def main():
    global N, nums
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        tmp = nums[i]
        idx = nums.index(nums[i])
        nums[idx] = -1
        ans = dfs([tmp], nums, 1)
        if ans != None:
            for i in range(N):
                print(ans[i], end=' ')
            break
        nums[idx] = tmp


def dfs(series, leftNum, cnt):
    global N
    if cnt == N:
        return series
    cur = series[cnt - 1]
    if cur * 2 in leftNum:
        idx = leftNum.index(cur * 2)
        leftNum[idx] = -1
        ans = dfs(series + [cur * 2], leftNum, cnt + 1)
        leftNum[idx] = cur * 2
        if ans != None:
            return ans
    if cur % 3 == 0 and cur // 3 in leftNum:
        idx = leftNum.index(cur // 3)
        leftNum[idx] = -1
        ans = dfs(series + [cur // 3], leftNum, cnt + 1)
        leftNum[idx] = cur // 3
        if ans != None:
            return ans


if __name__ == '__main__':
    main()
