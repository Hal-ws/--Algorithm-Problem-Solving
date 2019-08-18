def findSosu(list):
    minIdx = 0
    sosuList = []
    while (minIdx < len(list)):
        if (list[minIdx] != None):
            delIdx = minIdx
            addVal = list[minIdx]
            sosuList.append(list[minIdx])
            list[minIdx] = None
            while (delIdx < len(list)):
                if (list[delIdx] != None):
                    list[delIdx] = None
                delIdx += addVal
            minIdx += 1
        else:
            minIdx += 1
    return sosuList
i = 2
numberList = []
while(i <= 246912):
    numberList.append(i)
    i += 1
sosuList = findSosu(numberList)
while(True):
    N = int(input())
    if (N == 0):
        break
    if (N == 1):
        print(1)
    else:
        listN = []
        i = 0
        while (i <= 2 * N):
            if (sosuList[i] > N):
                firstIdx = i
                break
            i += 1
        while (True):
            if (sosuList[i] == sosuList[len(sosuList) - 1]):
                lastIdx = i
                break
            if (sosuList[i] > 2 * N):
                lastIdx = i - 1
                break
            i += 1
        print(lastIdx - firstIdx + 1)
