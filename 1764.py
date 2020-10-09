import sys

N, M = map(int, sys.stdin.readline().split())

def findcross(sList, lList):
    i = 0
    j = 0
    crossed = []
    while i < len(sList) and j < len(lList):
        if sList[i] == lList[j]:
            crossed.append(sList[i][:len(sList[i]) - 1])
            i += 1
            j += 1
        elif sList[i] > lList[j]:
            j += 1
        else:
            i += 1
    return crossed

dud = []
for i in range(N):
    dud.append(sys.stdin.readline())
dud = sorted(dud)

bo = []
for i in range(M):
    bo.append(sys.stdin.readline())
bo = sorted(bo)

if len(dud) >= len(bo):
    dudbo = findcross(bo, dud)
else:
    dudbo = findcross(dud, bo)

print(len(dudbo))
for i in range(len(dudbo)):
    print(dudbo[i])
