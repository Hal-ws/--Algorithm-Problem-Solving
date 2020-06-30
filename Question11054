import sys

def leftmax(temp, idx, val):
    a = 0
    for j in range(1, idx + 1):
        if temp[idx - j][0] < val and temp[idx - j][1] > a:
            a = temp[idx - j][1]
    return a
def rightmax(temp, idx, val):
    a = 0
    for j in range(N - idx - 1):
        if temp[j][0] < val and temp[j][2] > a:
            a = temp[j][2]
    return a

N = int(sys.stdin.readline())
series = list(map(int, sys.stdin.readline().split()))
series[0] = [series[0], 1, 0]
series[N - 1] = [series[N - 1], 0, 1]
for i in range(1, N - 1):
    series[i] = [series[i], 0, 0]
bitonics = [[0, 0] for i in range(N)]
bitonics[0][0] = 1
bitonics[N - 1][1] = 1


for i in range(1, N):
    temp = sorted(series[:i])
    left = leftmax(temp, i, series[i][0])
    if left == 0:
        series[i][1] = 1
        bitonics[i][0] = 1
    else:
        series[i][1] = left + 1
        bitonics[i][0] = left + 1
for i in range(2, N + 1):
    temp = sorted(series[N - i + 1:], reverse = True)
    right = rightmax(temp, N - i, series[N - i][0])
    if right == 0:
        series[N - i][2] = 1
        bitonics[N - i][1] = 1
    else:
        series[N - i][2] = right + 1
        bitonics[N - i][1] = right + 1
for i in range(N):
    bitonics[i] = bitonics[i][0] + bitonics[i][1] - 1
print(max(bitonics))
