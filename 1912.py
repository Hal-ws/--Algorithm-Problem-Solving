N = int(input())
series = list(map(int, input().split()))

maxVal = [0] * (N - 1) + [series[N - 1]]

for i in range(2, N + 1):
    if maxVal[N - i + 1] >= 0:
        maxVal[N - i] = maxVal[N - i + 1] + series[N - i]
    else:
        maxVal[N - i] = series[N - i]

print(max(maxVal))
