def main():
    N = int(input())
    nums = list(map(int, input().split()))
    start = [0] * N
    end = [0] * N
    start[N - 1], end[0] = nums[N - 1], nums[0]
    if N == 1:
        print(nums[0])
        return 0
    for i in range(N - 2, -1, -1):
        if start[i + 1] >= 0:
            start[i] = start[i + 1] + nums[i]
        else:
            start[i] = nums[i]
        if end[N - i - 2] >= 0:
            end[N - i - 1] = end[N - i - 2] + nums[N - i - 1]
        else:
            end[N - i - 1] = nums[N - i - 1]
    maxValwhole = start[0]
    maxValdel = start[1]
    for i in range(1, N - 1):
        if start[i] >= maxValwhole:
            maxValwhole = start[i]
        if end[i - 1] + start[i + 1] >= maxValdel:
            maxValdel = end[i - 1] + start[i + 1]
    if start[N - 1] >= maxValwhole:
        maxValwhole = start[N - 1]
    if end[N - 1] >= maxValdel:
        maxValdel = end[N - 1]
    print(max(maxValdel, maxValwhole))


if __name__ == "__main__":
    main()
