def main():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    sumList = [0] * N
    sameCnt = [0] * 1000
    ans = 0
    for i in range(N):
        sumList[i] = (nums[i] + sumList[i - 1]) % M
        sameCnt[sumList[i]] += 1
    ans += sameCnt[0]
    for i in range(1000):
        tmp = sameCnt[i]
        ans += (tmp * (tmp - 1)) // 2
    print(ans)
    return 0


if __name__ == "__main__":
    main()
