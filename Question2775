N = int(input())

i = 0
while(i < N):
    k = int(input())
    n = int(input())
    apart = []
    j = 0
    zeroFloor = []
    while(j < n):
        zeroFloor.append(j + 1)
        j += 1
    apart.append(zeroFloor)
    floorIdx = 1
    while(floorIdx <= k):
        if (floorIdx == 1):
            addedFloor = [1]
            l = 1
            while (l < n):
                addedFloor.append(addedFloor[l - 1] + apart[0][l])
                l += 1
            apart.append(addedFloor)
        else:
            l = 1
            addedFloor = [1]
            while (l < n):
                addedFloor.append(addedFloor[l - 1] + apart[floorIdx - 1][l])
                l += 1
            apart.append(addedFloor)
        floorIdx += 1
    print(apart[k][n - 1])
    i += 1
