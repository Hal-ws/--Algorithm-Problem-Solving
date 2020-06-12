T = int(input())

for j in range(T):
    n = int(input())
    ans = [0] * 10
    ans[0] = 1
    ans[1] = 2
    ans[2] = 4
    if n > 3:
        for i in range(3, n):
            ans[i] = ans[i - 3] + ans[i - 2] + ans[i - 1]
    print(ans[n - 1])
