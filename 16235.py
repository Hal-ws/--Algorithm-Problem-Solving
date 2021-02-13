import sys
from collections import deque


N, M, K = map(int, sys.stdin.readline().split())
dy, dx = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
ground = [[5 for j in range(N)] for i in range(N)]
trees = [[deque() for j in range(N)] for i in range(N)]
add, deadTree = [], []
for i in range(N):
    add.append(list(map(int, sys.stdin.readline().split())))
for i in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    trees[x - 1][y - 1].append(z)
for year in range(K):
    newTree = [[deque() for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            rotten = 0
            l = len(trees[i][j])
            spread = []
            for t in range(l):
                age = trees[i][j].popleft()
                if age <= ground[i][j]:
                    ground[i][j] -= age
                    newTree[i][j].append(age + 1)
                    if (age + 1) % 5 == 0:
                        spread.append(age + 1)
                else:
                    rotten += (age // 2)
            ground[i][j] += rotten
            for t in spread:
                for k in range(8):
                    ny, nx = i + dy[k], j + dx[k]
                    if 0 <= ny < N and 0 <= nx < N:
                        newTree[ny][nx].appendleft(1)
    trees = newTree
    for i in range(N):
        for j in range(N):
            ground[i][j] += add[i][j]
ans = 0
for i in range(N):
    for j in range(N):
        ans += len(trees[i][j])
print(ans)
