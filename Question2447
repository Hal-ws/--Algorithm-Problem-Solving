N = int(input())

def drawstar(size):
    if(size > 3):
        newList = [0] * size
        basicList = drawstar(size // 3)
        for i in range(size // 3):
            newList[i] = basicList[i] * 3
        for i in range(size // 3, size * 2 // 3):
            newList[i] = basicList[i - size // 3] + ' ' * (size // 3) + basicList[i - size // 3]
        for i in range(size * 2 // 3, size):
            newList[i] = newList[i - size // 3 * 2]
        return newList
    else:
        smallestList = ['***',
                     '* *',
                     '***']
        return smallestList

ans = drawstar(N)

for i in range(len(ans)):
    print(ans[i])
