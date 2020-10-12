from itertools import combinations

N, S = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0

for i in range(1, N + 1):
    temp = list(combinations(a, i))
    for j in range(len(temp)):
        if sum(temp[j]) == S:
            cnt += 1

print(cnt)
