import sys

N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(len(a)):
    sum = 0
    for j in range(i, len(a)):
        sum += a[j]
        if sum == M:
            cnt += 1
            break
        if sum > M:
            break

print(cnt)
