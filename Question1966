T = int(input())

def getMaxIdx(inputList):
    temp = []
    for i in range(len(inputList)):
        if type(inputList[i]) == int:
            temp.append(inputList[i])
        else:
            temp.append(inputList[i][1])
    return temp.index(max(temp))

def printpaper(inputList):
    cnt = 0
    while True:
        inputList += inputList[:getMaxIdx(inputList)]
        for j in range(getMaxIdx(inputList)):
            inputList.remove(inputList[0])
        if type(inputList[0]) == int:
            inputList.remove(inputList[0])
            cnt += 1
        else:
            cnt += 1
            break
    return cnt

for i in range(T):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    importance[M] = [M, importance[M]]
    print(printpaper(importance))
