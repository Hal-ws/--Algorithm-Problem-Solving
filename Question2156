import sys
N = int(sys.stdin.readline())
wines = [0] * N
for i in range(N):
    wines[i] = int(sys.stdin.readline())


if N > 3:
    dp = [[0, 0, wines[0]], [0, wines[1], wines[0] + wines[1]], [wines[2], wines[0] + wines[2], wines[1] + wines[2]]]
    for i in range(3, N):
        temp = [0, 0, 0]
        temp[0] = max(dp[i - 3]) + wines[i]
        temp[1] = max(dp[i - 2]) + wines[i]
        temp[2] = max(dp[i - 1][1], dp[i - 1][0]) + wines[i]
        dp.append(temp)
    print(max(max(dp[N - 1]), max(dp[N - 2])))
elif N == 1:
    print(wines[0])
elif N == 2:
    print(wines[0] + wines[1])
else:
    print(max(wines[0] + wines[1], wines[0] + wines[2], wines[1] + wines[2]))
