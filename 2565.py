import sys

def findmax(temp, idx, val):
    a = 0
    for j in range(1, idx + 1):
        if temp[idx - j][0] < val and temp[idx - j][1] > a:
            a = temp[idx - j][1]
    return a

N = int(sys.stdin.readline())
lines = [0] * N
for i in range(N):
    lines[i] = list(map(int, sys.stdin.readline().split()))
lines = sorted(lines)
series = [0] * N
series[0] = [lines[0][1], 1]
for i in range(1, N):
    series[i] = [lines[i][1], 0]
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

print(N - max(maxLen))
