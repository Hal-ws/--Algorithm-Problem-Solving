T = int(input())

for j in range(T):
    n = int(input())
    ans = [0] * 3
    ans[0] = 1
    ans[1] = 2
    ans[2] = 4
    if n > 3:
        for i in range(3, n):
            temp = (ans[2] + ans[1] + ans[0]) % 1000000009
            ans[0] = ans[1]
            ans[1] = ans[2]
            ans[2] = temp
        print(ans[2])
    else:
        print(ans[n - 1])
