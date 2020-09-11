import sys
ansList = []
for i in range(4):
    a, b = map(int, sys.stdin.readline().split())
    if i == 0:
        ansList.append(b - a)
    else:
        ansList.append(ansList[i - 1] + (b - a))
print(max(ansList))
