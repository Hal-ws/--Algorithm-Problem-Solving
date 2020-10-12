a = list(map(int, input().split()))

def setNumber(list, startIdx, num):
    for i in range(startIdx, len(list)):
        list[i] = num
    return list

numList = []

for i in range(a[1]):
    numList.append(1)

while True:
    for i in range(len(numList)):
        print(numList[i], end=' ')
    print('')
    if numList[0] == a[0] and numList[len(numList) - 1] == a[0]:
        break
    numList[len(numList) - 1] += 1
    for i in range(a[1] - 1):
        if a[1] == 1:
            break
        if numList[a[1] - i - 1] == a[0]:
            for j in range(len(numList)):
                print(numList[j], end=' ')
            print('')
            numList[a[1] - i - 2] += 1
            numList = setNumber(numList, a[1] - i - 1, numList[a[1] - i - 2])
