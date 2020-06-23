import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
cost = []
for i in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))
memo = [[cost[0][0], cost[0][1], cost[0][2]]]
for idx in range(1, N):
    memo.append([min([memo[idx - 1][1], memo[idx - 1][2]])  + cost[idx][0], min([memo[idx - 1][0], memo[idx - 1][2]])  + cost[idx][1], min([memo[idx - 1][0], memo[idx - 1][1]])  + cost[idx][2]])
print(min(memo[N - 1]))
