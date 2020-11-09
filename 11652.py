import sys


def main():
    N = int(sys.stdin.readline())
    nums = [0] * N
    for i in range(N):
        nums[i] = int(sys.stdin.readline())
    nums = sorted(nums, reverse=True)
    maxCnt = 1
    maxVal = nums[0]
    tempCnt = 1
    for i in range(N):
        if i > 0:
            if nums[i] == nums[i - 1]:
                tempCnt += 1
            else:
                if tempCnt >= maxCnt:
                    maxCnt = tempCnt
                    maxVal = nums[i - 1]
                tempCnt = 1
        if i == N - 1:
            if tempCnt >= maxCnt:
                maxCnt = tempCnt
                maxVal = nums[i]
    print(maxVal)


if __name__ == "__main__":
    main()
