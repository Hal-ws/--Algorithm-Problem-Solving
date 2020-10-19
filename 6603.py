import sys
from itertools import combinations

while True:
    tcase = list(map(int, input().split()))
    if tcase[0] == 0:
        break
    numcnt = tcase[0]
    numList = tcase[1:]
    ansList = list(combinations(numList, 6))
    la = len(ansList)
    for i in range(la):
        for j in range(6):
            print(ansList[i][j], end= ' ')
        print()
    print()
