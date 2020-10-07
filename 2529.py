from itertools import combinations

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
ansList = list(combinations(num, M))
la = len(ansList)
for i in range(la):
    for j in range(M):
        print(ansList[i][j], end = ' ')
    print()
