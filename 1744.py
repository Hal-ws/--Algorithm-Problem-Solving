import sys


def main():
    N = int(sys.stdin.readline())
    nums = [0] * N
    for i in range(N):
        nums[i] = int(sys.stdin.readline())
    ans = 0
    nums.sort(reverse=True)
    i = 0
    while i < N - 1:
        if nums[i] > 0:
            if nums[i + 1] > 0:
                if nums[i] == 1 or nums[i + 1] == 1:
                    ans += (nums[i] + nums[i + 1])
                else:
                    ans += nums[i] * nums[i + 1]
                i += 2
            else:
                ans += nums[i]
                break
        else:
            break
    if N % 2 == 1 and nums[N - 1] > 0:
        ans += nums[N - 1]
    i = N - 1
    while i > 0:
        if nums[i] < 0:
            if nums[i - 1] < 0:
                ans += nums[i] * nums[i - 1]
                i -= 2
            elif nums[i - 1] == 0:
                break
            else:
                ans += nums[i]
                break
        else:
            break
    if N % 2 == 1 and nums[0] < 0:
        ans += nums[0]
    print(ans)


if __name__ == "__main__":
    main()
