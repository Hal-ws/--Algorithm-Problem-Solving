N, M = map(int, input().split())

def checkUpIdx(idxList, maxIdxList):
    for i in range(len(idxList)):
        if idxList[i] > maxIdxList[i]:
            return i
    return None

numList = [0] * N
for i in range(N):
    numList[i] = i + 1

idxList = [0] * M
for i in range(M):
    idxList[i] = i

maxIdxList = [0] * M
for i in range(M):
    maxIdxList[i] = N - M + i

while 1:
    ansList = [0] * M
    for i in range(M):
        ansList[i] = numList[idxList[i]]
    for i in range(M):
        print(ansList[i], end=' ')
    print()
    idxList[len(idxList) - 1] += 1
    for i in range(M - 1):
        if idxList[M - 1 - i] > maxIdxList[M - 1 -i]: ##
            idxList[M - 2 - i] += 1
    upStdIdx = checkUpIdx(idxList, maxIdxList) ## 올려줘야할 idx가 있는지 판단
    if upStdIdx != None and upStdIdx != 0:
        for i in range(upStdIdx, M):
            idxList[i] = idxList[i - 1] + 1
    elif upStdIdx == 0:
        break
    if idxList[0] >= N - M:
        if N == 1:
            break
        for i in range(M):
            ansList[i] = numList[idxList[i]]
        for i in range(M):
            print(ansList[i], end=' ')
        break
