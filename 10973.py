def main():
    N = int(input())
    nums = list(map(int, input().split()))
    adding = []
    flag = 0
    for i in range(N - 1, 0, -1):
        if nums[i] < nums[i - 1]:
            flag = 1
            stdIdx = i - 1
            maxVal = 0
            for j in range(stdIdx + 1, N):
                if nums[j] < nums[stdIdx] and nums[j] > maxVal:
                    maxVal = nums[j]
        adding.append(nums[i])
        if flag == 1:
            break
    if flag == 0:
        print(-1)
    else:
        adding.append(nums[stdIdx])
        adding.remove(maxVal)
        ans = nums[:stdIdx] + [maxVal] + sorted(adding, reverse=True)
        for i in range(N):
            print(ans[i], end= ' ')


if __name__ == "__main__":
    main()
