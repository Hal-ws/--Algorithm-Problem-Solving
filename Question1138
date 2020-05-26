import sys

N = int(sys.stdin.readline())
hint = list(map(int, sys.stdin.readline().split()))
ans = [N]
for i in range(2, N + 1):
    ans.insert(hint[N - i], N - i + 1)

for i in range(N):
    print(ans[i], end = ' ')
