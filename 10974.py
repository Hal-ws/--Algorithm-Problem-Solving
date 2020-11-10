def main():
    N = int(input())
    nums = [0] * N
    for i in range(N):
        nums[i] = i + 1
    for i in range(N):
        print(nums[i], end=' ')
    print()
    while 1:
        nums = getnext(nums, N)
        if nums == False:
            break
        else:
            for i in range(N):
                print(nums[i], end=' ')
            print()


def getnext(nums, N):
    adding = []
    flag = 0
    for i in range(N - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            flag = 1
            stdIdx = i - 1
            minVal = 10001
            for j in range(stdIdx + 1, N):
                if nums[j] > nums[stdIdx] and nums[j] <= minVal:
                    minVal = nums[j]
        adding.append(nums[i])
        if flag == 1:
            break
    if flag == 0:
        return False
    else:
        adding.append(nums[stdIdx])
        adding.remove(minVal)
        ans = nums[:stdIdx] + [minVal] + sorted(adding)
    return ans


if __name__ == "__main__":
    main()
