def main():
    minV, maxV = map(int, input().split())
    nums = []
    for i in range(2, 1000001):
        nums.append(i * i)
    ans = [1] * (maxV - minV + 1)
    for n in nums:
        if n > maxV:
            break
        if minV % n == 0:
            sIdx = minV // n
        else:
            sIdx = (minV // n) + 1
        eIdx = maxV // n
        for i in range(sIdx, eIdx + 1):
            ans[n * i - minV] = 0
    print(sum(ans))


if __name__ == '__main__':
    main()
