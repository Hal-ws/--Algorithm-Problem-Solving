N, M = map(int, input().split())

def factorial(N, M):
    ans = 1
    for i in range(M):
        ans *= N - i
    return ans

def removeduplicated(elementList, numList):
    tempList = [0] * len(numList)
    for i in range(len(numList)):
        tempList[i]  = numList[i]
    for i in range(len(elementList)):
        if elementList[i] in tempList:
            tempList.remove(elementList[i])
    return tempList

numList = [0] * N
for i in range(N):
    numList[i] = i + 1
maxLen = factorial(N, M)
ansList = [[0 for j in range(M)] for i in range(maxLen)]
for j in range(M):
    tempIdx = 0
    for i in range(maxLen):
        temp = removeduplicated(ansList[i], numList)
        maxTempIdx = len(temp)
        if i != 0 and i % (maxLen // factorial(N, j + 1)) == 0:
            tempIdx += 1
        if tempIdx == maxTempIdx:
            tempIdx = 0
        ansList[i][j] = temp[tempIdx]
    if ansList[len(ansList) - 1][M - 1] != 0:
        break

for i in range(len(ansList)):
    for j in range(len(ansList[i])):
        print(ansList[i][j], end = ' ')
    print()
