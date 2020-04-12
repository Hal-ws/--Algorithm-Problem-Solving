import sys

N = int(sys.stdin.readline())
F = int(sys.stdin.readline())

N = N // 100 * 100
for i in range(100):
    if N % F == 0:
        break
    N += 1

ans = str(N % 100)
if len(ans) == 1:
    print('0' + ans)
else:
    print(ans)
