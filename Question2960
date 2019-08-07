N, K = map(int, input().split())
list = []
i = 2

while(i <= N):  ## 2부터 N까지 값을 배치
    list.append(i)
    i += 1

minIdx = 0
deletedList = []
while(minIdx < len(list)):
    if(list[minIdx] != None): ## minIdx의 자리가 비어있지 않다면 삭제 수행
        delIdx = minIdx
        deletedList.append(list[minIdx])
        addVal = list[minIdx]
        list[minIdx] = None
        while(delIdx < len(list)):
            if(list[delIdx] != None):
                deletedList.append(list[delIdx])
                list[delIdx] = None
            delIdx += addVal
        minIdx += 1
    else:
        minIdx += 1

print(deletedList[K - 1])
