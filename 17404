import sys

N = int(sys.stdin.readline())
cost = []
for i in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))

r = [cost[0][0]] ## RED로 시작
g = [cost[0][1]] ## Green으로 시작
b = [cost[0][2]] ## Blue로 시작
for idx in range(1, N):
    if idx == 1:
        r.append([None,r[0] + cost[idx][1], r[0] + cost[idx][2]])
        g.append([g[0] + cost[idx][0], None, g[0] + cost[idx][2]])
        b.append([b[0] + cost[idx][0], b[0] + cost[idx][1], None])
    elif idx == 2:
        r.append([min(r[idx - 1][1], r[idx - 1][2]) + cost[idx][0], r[idx - 1][2] + cost[idx][1],
                  r[idx - 1][1] + cost[idx][2]])
        g.append([g[idx - 1][2] + cost[idx][0], min(g[idx - 1][0], g[idx - 1][2]) + cost[idx][1],
                  g[idx - 1][0] + cost[idx][2]])
        b.append([b[idx - 1][1] + cost[idx][0], b[idx - 1][0] + cost[idx][1],
                  min(b[idx - 1][0], b[idx - 1][1]) + cost[idx][2]])
    else:
        r.append([min(r[idx - 1][1], r[idx - 1][2]) + cost[idx][0], min(r[idx - 1][0], r[idx - 1][2]) + cost[idx][1],
                  min(r[idx - 1][0], r[idx - 1][1]) + cost[idx][2]])
        g.append([min(g[idx - 1][1], g[idx - 1][2]) + cost[idx][0], min(g[idx - 1][0], g[idx - 1][2]) + cost[idx][1],
                  min(g[idx - 1][0], g[idx - 1][1]) + cost[idx][2]])
        b.append([min(b[idx - 1][1], b[idx - 1][2]) + cost[idx][0], min(b[idx - 1][0], b[idx - 1][2]) + cost[idx][1],
                  min(b[idx - 1][0], b[idx - 1][1]) + cost[idx][2]])
ans = [min(r[N - 1][1], r[N - 1][2]), min(g[N - 1][0], g[N - 1][2]), min(b[N - 1][0], b[N - 1][1])]
print(min(ans))
