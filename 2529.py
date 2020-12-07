def main():
    K = int(input())
    signs = list(map(str, input().split()))
    ans = [0, 9999999999, 0, 0]
    lower, upper = 9 - K, 9
    for i in range(lower, upper + 1):
        used = [0] * 10
        used[i] = 1
        dfs(signs, str(i), used, 1, i, lower, upper, ans)
    lower, upper = 0, K
    for i in range(lower, upper + 1):
        used = [0] * (K + 1)
        used[i] = 1
        dfs(signs, str(i), used, 1, i, lower, upper, ans)
    print(ans[2])
    print(ans[3])

def dfs(signs, cur, used, level, before, lower, upper, ans): #cur: 현재까지 만든 숫자(str형)
    if level == upper - lower + 1:
        result = int(cur)
        if result >= ans[0]:
            ans[0] = result
            ans[2] = cur
        if result <= ans[1]:
            ans[1] = result
            ans[3] = cur
        return
    for i in range(lower, upper + 1):
        num = i # 새로 추가할 number
        if used[num] == 0: # 안쓴 숫자인지 확인
            if before < num and signs[level - 1] == "<":
                used[num] = 1
                dfs(signs, cur + str(num), used, level + 1, num, lower, upper, ans)
                used[num] = 0
            if before > num and signs[level - 1] == ">":
                used[num] = 1
                dfs(signs, cur + str(num), used, level + 1, num, lower, upper, ans)
                used[num] = 0


if __name__ == "__main__":
    main()
