import sys

N, M = map(int, sys.stdin.readline().split())
ans = [1] * (M - 1) + [0]

for i in range(N ** M):
    ans[M - 1] += 1
    for j in range(M):
        if ans[M - 1- j] == N + 1:
            ans[M - 1 - j] = 1
            ans[M - 1 - j - 1] += 1
    for j in range(M):
        print(ans[j], end = ' ')
    print()
