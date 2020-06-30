import sys


def findmax(temp, idx, val):
    a = 0
    for j in range(1, idx + 1):
        if temp[idx - j][0] < val and temp[idx - j][1] > a:
            a = temp[idx - j][1]
    return a

N = int(sys.stdin.readline())

series = list(map(int, sys.stdin.readline().split()))
series[0] = [series[0], 1]
for i in range(1, N):
    series[i] = [series[i], 0]
maxLen = [1] + [0] * (N - 1)

for i in range(1, N):
    temp = sorted(series[:i])
    check = findmax(temp, i, series[i][0])
    if check == 0:
        series[i][1] = 1
        maxLen[i] = 1
    else:
        series[i][1] = check + 1
        maxLen[i] = check + 1
print(max(maxLen))
