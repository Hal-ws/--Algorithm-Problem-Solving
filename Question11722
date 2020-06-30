N = int(input())

def rightmax(temp, idx, val): ## 오른쪽에 있는 감소수열 길이 max값 측정
    a = 0
    for j in range(N - idx - 1):
        if temp[j][0] < val and temp[j][1] > a:
            a = temp[j][1]
    return a

series = list(map(int, input().split()))
series[N - 1] = [series[N - 1], 1] ## [N번째 값, 해당 값이 시작점인 감소수열의 길이]
for i in range(0, N - 1):
    series[i] = [series[i], 0]

maxLen = [0] * (N - 1) + [1]

for i in range(2, N + 1):
    temp = sorted(series[N - i + 1:], reverse = True)
    check = rightmax(temp, N - i, series[N - i][0])
    if check == 0:
        series[N - i][1] = 1
        maxLen[N - i] = 1
    else:
        series[N - i][1] = check + 1
        maxLen[N - i] = check + 1

print(max(maxLen))
