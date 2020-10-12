a, b = map(int, input().split())

ans = str(a + b)

for i in range(1, len(ans)):
    if int(ans[len(ans) - i]) >= 2:
        ans = ans[:len(ans) - i - 1] + str(int(ans[len(ans) - i - 1]) + 1) + str(int(ans[len(ans) - i]) % 2) + ans[len(ans) - i + 1:]
if ans[0] == '2' or ans[0] == '3':
    ans = '1' + str(int(ans[0]) % 2) + ans[1:]
print(ans)
