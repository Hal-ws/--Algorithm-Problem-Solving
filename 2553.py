N = int(input())
ans = 1
for i in range(2, N + 1):
    ans = ans * i
    ans = ans % 100000000
    while ans % 10 == 0:
        ans = ans // 10
print(ans % 10)
