def main():
    N = int(input())
    cnt = [0] * (1000001)
    ans = [0] * N
    stack = []
    nList = list(map(int, input().split()))
    for num in nList:
        cnt[num] += 1
    ans[N - 1] = -1
    stack.append(nList[N - 1])
    for i in range(N - 2, -1, -1):
        num = nList[i]
        flag = 0
        nCnt = cnt[num]
        while len(stack) > 0:
            tNum = stack.pop()
            tCnt = cnt[tNum]
            if nCnt < tCnt:
                flag = 1
                ans[i] = tNum
                stack.append(tNum)
                stack.append(num)
                break
        if flag == 0:
            ans[i] = -1
            stack.append(num)
    for i in range(N):
        print(ans[i], end=' ')


if __name__ == '__main__':
    main()
