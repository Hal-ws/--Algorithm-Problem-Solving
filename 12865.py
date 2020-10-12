import sys

N, K = map(int, sys.stdin.readline().split())
stuffs = []

for i in range(N):
    stuffs.append(list(map(int, sys.stdin.readline().split())))

dp = []
dp.append([0] * (K + 1))
for i in range(1, N + 1):
    temp = [0] * (K + 1)
    for j in range(K + 1):
        if j >= stuffs[i - 1][0]:
            temp[j] = max(dp[i - 1][j], stuffs[i - 1][1] + dp[i - 1][j - stuffs[i - 1][0]])
        else:
            temp[j] = dp[i - 1][j]
    dp.append(temp)


ans = 0
for i in range(N + 1):
    if max(dp[i]) >= ans:
        ans = max(dp[i])

print(ans)
