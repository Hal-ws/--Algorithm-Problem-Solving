def main():
    N = int(input())
    nList = list(map(int, input().split()))
    stack = []
    ans = [0] * N
    ans[N - 1] = -1
    stack.append(nList[N - 1])
    for i in range(N - 2, -1, -1):
        num = nList[i]
        flag = 0 #못찾은 상태
        while len(stack) > 0:
            tmp = stack.pop()
            if num < tmp:
                flag = 1
                ans[i] = tmp
                stack.append(tmp)
                stack.append(num)
                break
        if flag == 0:
            ans[i] = -1
            stack.append(num)
    for i in range(N):
        print(ans[i], end=' ')


if __name__ == '__main__':
    main()
